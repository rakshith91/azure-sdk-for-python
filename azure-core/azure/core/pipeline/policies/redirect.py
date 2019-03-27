# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------
"""
This module is the requests implementation of Pipeline ABC
"""
from __future__ import absolute_import  # we have a "requests" module that conflicts with "requests" on Py2.7
import contextlib
import logging
import threading
from typing import TYPE_CHECKING, List, Callable, Iterator, Any, Union, Dict, Optional  # pylint: disable=unused-import
import warnings
try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse

from azure.core.exceptions import (
    ClientRequestError,
    TooManyRedirectsError
)

from .base import HTTPPolicy, RequestHistory


_LOGGER = logging.getLogger(__name__)


class RedirectPolicy(HTTPPolicy):
    """A redirect policy"""

    REDIRECT_STATUSES = frozenset([301, 302, 303, 307, 308])

    REDIRECT_HEADERS_BLACKLIST = frozenset(['Authorization'])

    def __init__(self, **kwargs):
        self.allow = kwargs.get('redirects_allow', True)
        self.max_redirects = kwargs.get('redirect_max', 30)

        remove_headers = set(kwargs.get('redirect_remove_headers', []))
        self._remove_headers_on_redirect = remove_headers.union(self.REDIRECT_HEADERS_BLACKLIST)
        redirect_status = set(kwargs.get('redirect_on_status_codes', []))
        self._redirect_on_status_codes = redirect_status.union(self.REDIRECT_STATUSES)

    @classmethod
    def no_redirects(cls):
        return cls(redirects_allow=False)

    def configure_redirects(self, **kwargs):
        return {
            'allow': kwargs.pop("redirects_allow", self.max_redirects),
            'redirects': kwargs.pop("redirect_max", self.max_redirects),
            'history': []
        }

    def get_redirect_location(self, response):
        """Should we redirect and where to?

        :returns: Truthy redirect location string if we got a redirect status
            code and valid location. ``None`` if redirect status and no
            location. ``False`` if not a redirect status code.
        """
        if response.http_response.status_code in self._redirect_on_status_codes \
                and response.http_request.method in ['GET', 'HEAD']:
            return response.http_response.headers.get('location')

        return False

    def increment(self, settings, response, redirect_location):
        """Increment the redirect attempts for this request.

        :param response: A pipeline response object.
        :param redirect_location: The redirected endpoint.

        :return: Whether further redirect attempts are remaining.
        """
        # TODO: Revise some of the logic here.
        settings['redirects'] -= 1
        settings['history'].append(RequestHistory(response.http_request, http_response=response.http_response))
        
        redirected = urlparse(redirect_location)
        if not redirected.netloc:
            base_url = urlparse(response.http_request.url)
            response.http_request.url = "{}://{}/{}".format(
                base_url.scheme,
                base_url.netloc,
                redirect_location.lstrip('/'))
        else:
            response.http_request.url = redirect_location
        if response.http_response.status_code == 303:
            response.http_request.method = 'GET'
        for non_redirect_header in self._remove_headers_on_redirect:
            response.http_request.headers.pop(non_redirect_header, None)
        return settings['redirects'] > 0 or not settings['allow']

    def send(self, request, **kwargs):
        retryable = True
        redirect_settings = self.configure_redirects(**kwargs)
        while retryable:
            response = self.next.send(request, **kwargs)
            redirect_location = self.get_redirect_location(response)
            if redirect_location:
                retryable = self.increment(redirect_settings, response, redirect_location)
                request.http_request = response.http_request
                continue
            return response

        raise TooManyRedirectsError(redirect_settings['history'])
