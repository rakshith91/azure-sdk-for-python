# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse  # type: ignore

from azure.servicebus.management._models import DictMixin

class ServiceBusConnectionStringProperties(DictMixin):
    """
    Properties of a connection string.
    """
    def __init__(self, **kwargs):
        self._fully_qualified_namespace = kwargs.pop('fully_qualified_namespace', None)
        self._endpoint = kwargs.pop('endpoint', None)
        self._entity_path = kwargs.pop('entity_path', None)
        self._shared_access_signature = kwargs.pop('shared_access_signature', None)
        self._shared_access_key_name = kwargs.pop('shared_access_key_name', None)
        self._shared_access_key = kwargs.pop('shared_access_key', None)
    
    @property
    def fully_qualified_namespace(self):
        """The fully qualified host name for the Service Bus namespace.
        The namespace format is: `<yournamespace>.servicebus.windows.net`.
        """
        return self._fully_qualified_namespace

    @property
    def endpoint(self):
        """The endpoint for the Service Bus resource. In the format sb://<FQDN>/
        """
        return self._endpoint

    @property
    def entity_path(self):
        """Optional. Represents the name of the queue/topic.
        """
        return self._entity_path

    @property
    def shared_access_signature(self):
        """
        This can be provided instead of the shared_access_key_name and the shared_access_key.
        """
        return self._shared_access_signature

    @property
    def shared_access_key_name(self):
        """
        The name of the shared access key.
        """
        return self._shared_access_key_name

    @property
    def shared_access_key(self):
        """
        Required for authentication along with the key name. A shared_access_signature can be used
        alternatively.
        """
        return self._shared_access_key

class ServiceBusConnectionStringParser(object):
    """Parse the connection string.

    :param conn_str: The connection string that has to be parsed.
    """
    def __init__(self, conn_str):
        # type: (str) -> None
        """
        :param conn_str: The connection string to parse.
        :type conn_str: str
        """
        self._conn_str = conn_str

    def parse(self):
        # type() -> ServiceBusConnectionStringProperties
        """
        Parse the connection string.
        """
        conn_str = self._conn_str.rstrip(";")
        conn_settings = [s.split("=", 1) for s in conn_str.split(";")]
        if any(len(tup) != 2 for tup in conn_settings):
            raise ValueError("Connection string is either blank or malformed.")
        conn_settings = dict(conn_settings)
        shared_access_signature = None
        for key, value in conn_settings.items():
            if key.lower() == 'sharedaccesssignature':
                shared_access_signature = value
        shared_access_key = conn_settings.get('SharedAccessKey')
        if shared_access_signature is not None and shared_access_key is not None:
            raise ValueError("Only one of the SharedAccessKey or SharedAccessSignature must be present.")
        endpoint = conn_settings.get('Endpoint')
        if not endpoint:
            raise ValueError("Connection string is either blank or malformed.")
        parsed = urlparse(endpoint.rstrip('/'))
        if not parsed.netloc:
            raise ValueError("Invalid Endpoint on the Connection String.")
        namespace = parsed.netloc.strip()
        props = {
            'fully_qualified_namespace': namespace,
            'endpoint': endpoint,
            'entity_path': conn_settings.get('EntityPath'),
            'shared_access_signature': shared_access_signature,
            'shared_access_key_name': conn_settings.get('SharedAccessKeyName'),
            'shared_access_key': shared_access_key
        }
        return ServiceBusConnectionStringProperties(**props)
