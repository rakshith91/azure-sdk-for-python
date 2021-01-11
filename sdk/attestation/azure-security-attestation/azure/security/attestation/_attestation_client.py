# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.0.6272, generator: {generator})
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.core import PipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any

from ._configuration import AttestationClientConfiguration
from .operations import PolicyOperations
from .operations import PolicyCertificatesOperations
from .operations import AttestationOperations
from .operations import SigningCertificatesOperations
from .operations import MetadataConfigurationOperations
from . import models


class AttestationClient(object):
    """Describes the interface for the per-tenant enclave service.

    :ivar policy: PolicyOperations operations
    :vartype policy: attestation_client.operations.PolicyOperations
    :ivar policy_certificates: PolicyCertificatesOperations operations
    :vartype policy_certificates: attestation_client.operations.PolicyCertificatesOperations
    :ivar attestation: AttestationOperations operations
    :vartype attestation: attestation_client.operations.AttestationOperations
    :ivar signing_certificates: SigningCertificatesOperations operations
    :vartype signing_certificates: attestation_client.operations.SigningCertificatesOperations
    :ivar metadata_configuration: MetadataConfigurationOperations operations
    :vartype metadata_configuration: attestation_client.operations.MetadataConfigurationOperations
    :param instance_url: The attestation instance base URI, for example https://mytenant.attest.azure.net.
    :type instance_url: str
    """

    def __init__(
        self,
        instance_url,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        base_url = '{instanceUrl}'
        self._config = AttestationClientConfiguration(instance_url, **kwargs)
        self._client = PipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.policy = PolicyOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.policy_certificates = PolicyCertificatesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.attestation = AttestationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.signing_certificates = SigningCertificatesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.metadata_configuration = MetadataConfigurationOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> AttestationClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
