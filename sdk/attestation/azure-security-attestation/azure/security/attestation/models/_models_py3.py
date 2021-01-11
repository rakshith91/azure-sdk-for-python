# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.0.6272, generator: {generator})
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Optional

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class AttestationPolicy(msrest.serialization.Model):
    """AttestationPolicy.

    :param policy: JSON Web Token whose body is an AttestationPolicyRequest definition.
    :type policy: str
    """

    _attribute_map = {
        'policy': {'key': 'policy', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        policy: Optional[str] = None,
        **kwargs
    ):
        super(AttestationPolicy, self).__init__(**kwargs)
        self.policy = policy


class CloudError(msrest.serialization.Model):
    """An error response from Attestation.

    :param error: An error response from Attestation.
    :type error: ~attestation_client.models.CloudErrorBody
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'CloudErrorBody'},
    }

    def __init__(
        self,
        *,
        error: Optional["CloudErrorBody"] = None,
        **kwargs
    ):
        super(CloudError, self).__init__(**kwargs)
        self.error = error


class CloudErrorBody(msrest.serialization.Model):
    """An error response from Attestation.

    :param code: An identifier for the error. Codes are invariant and are intended to be consumed
     programmatically.
    :type code: str
    :param message: A message describing the error, intended to be suitable for displaying in a
     user interface.
    :type message: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        code: Optional[str] = None,
        message: Optional[str] = None,
        **kwargs
    ):
        super(CloudErrorBody, self).__init__(**kwargs)
        self.code = code
        self.message = message
