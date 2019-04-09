# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

try:
    from .error_field_contract_py3 import ErrorFieldContract
    from .error_response_body_py3 import ErrorResponseBody
    from .error_response_py3 import ErrorResponse, ErrorResponseException
    from .region_contract_py3 import RegionContract
    from .resource_py3 import Resource
    from .api_export_result_py3 import ApiExportResult
    from .product_entity_base_parameters_py3 import ProductEntityBaseParameters
    from .product_tag_resource_contract_properties_py3 import ProductTagResourceContractProperties
    from .operation_tag_resource_contract_properties_py3 import OperationTagResourceContractProperties
    from .subscription_key_parameter_names_contract_py3 import SubscriptionKeyParameterNamesContract
    from .open_id_authentication_settings_contract_py3 import OpenIdAuthenticationSettingsContract
    from .oauth2_authentication_settings_contract_py3 import OAuth2AuthenticationSettingsContract
    from .authentication_settings_contract_py3 import AuthenticationSettingsContract
    from .api_version_set_contract_details_py3 import ApiVersionSetContractDetails
    from .api_create_or_update_properties_wsdl_selector_py3 import ApiCreateOrUpdatePropertiesWsdlSelector
    from .api_contract_properties_py3 import ApiContractProperties
    from .api_entity_base_contract_py3 import ApiEntityBaseContract
    from .api_tag_resource_contract_properties_py3 import ApiTagResourceContractProperties
    from .tag_tag_resource_contract_properties_py3 import TagTagResourceContractProperties
    from .tag_resource_contract_py3 import TagResourceContract
    from .tag_contract_py3 import TagContract
    from .tag_description_contract_py3 import TagDescriptionContract
    from .tag_description_create_parameters_py3 import TagDescriptionCreateParameters
    from .issue_attachment_contract_py3 import IssueAttachmentContract
    from .issue_comment_contract_py3 import IssueCommentContract
    from .issue_contract_base_properties_py3 import IssueContractBaseProperties
    from .issue_update_contract_py3 import IssueUpdateContract
    from .issue_contract_py3 import IssueContract
    from .body_diagnostic_settings_py3 import BodyDiagnosticSettings
    from .http_message_diagnostic_py3 import HttpMessageDiagnostic
    from .pipeline_diagnostic_settings_py3 import PipelineDiagnosticSettings
    from .sampling_settings_py3 import SamplingSettings
    from .diagnostic_contract_py3 import DiagnosticContract
    from .schema_contract_py3 import SchemaContract
    from .policy_contract_py3 import PolicyContract
    from .policy_collection_py3 import PolicyCollection
    from .product_contract_py3 import ProductContract
    from .parameter_contract_py3 import ParameterContract
    from .representation_contract_py3 import RepresentationContract
    from .response_contract_py3 import ResponseContract
    from .request_contract_py3 import RequestContract
    from .operation_entity_base_contract_py3 import OperationEntityBaseContract
    from .operation_update_contract_py3 import OperationUpdateContract
    from .operation_contract_py3 import OperationContract
    from .api_release_contract_py3 import ApiReleaseContract
    from .api_revision_contract_py3 import ApiRevisionContract
    from .api_update_contract_py3 import ApiUpdateContract
    from .api_contract_py3 import ApiContract
    from .api_create_or_update_parameter_py3 import ApiCreateOrUpdateParameter
    from .api_version_set_entity_base_py3 import ApiVersionSetEntityBase
    from .api_version_set_update_parameters_py3 import ApiVersionSetUpdateParameters
    from .api_version_set_contract_py3 import ApiVersionSetContract
    from .token_body_parameter_contract_py3 import TokenBodyParameterContract
    from .authorization_server_contract_base_properties_py3 import AuthorizationServerContractBaseProperties
    from .authorization_server_update_contract_py3 import AuthorizationServerUpdateContract
    from .authorization_server_contract_py3 import AuthorizationServerContract
    from .backend_reconnect_contract_py3 import BackendReconnectContract
    from .backend_tls_properties_py3 import BackendTlsProperties
    from .backend_proxy_contract_py3 import BackendProxyContract
    from .backend_authorization_header_credentials_py3 import BackendAuthorizationHeaderCredentials
    from .backend_credentials_contract_py3 import BackendCredentialsContract
    from .x509_certificate_name_py3 import X509CertificateName
    from .backend_service_fabric_cluster_properties_py3 import BackendServiceFabricClusterProperties
    from .backend_properties_py3 import BackendProperties
    from .backend_base_parameters_py3 import BackendBaseParameters
    from .backend_update_parameters_py3 import BackendUpdateParameters
    from .backend_contract_py3 import BackendContract
    from .cache_update_parameters_py3 import CacheUpdateParameters
    from .cache_contract_py3 import CacheContract
    from .certificate_contract_py3 import CertificateContract
    from .certificate_create_or_update_parameters_py3 import CertificateCreateOrUpdateParameters
    from .resource_sku_py3 import ResourceSku
    from .resource_sku_capacity_py3 import ResourceSkuCapacity
    from .resource_sku_result_py3 import ResourceSkuResult
    from .certificate_information_py3 import CertificateInformation
    from .certificate_configuration_py3 import CertificateConfiguration
    from .hostname_configuration_py3 import HostnameConfiguration
    from .virtual_network_configuration_py3 import VirtualNetworkConfiguration
    from .api_management_service_sku_properties_py3 import ApiManagementServiceSkuProperties
    from .additional_location_py3 import AdditionalLocation
    from .api_management_service_backup_restore_parameters_py3 import ApiManagementServiceBackupRestoreParameters
    from .api_management_service_base_properties_py3 import ApiManagementServiceBaseProperties
    from .api_management_service_identity_py3 import ApiManagementServiceIdentity
    from .api_management_service_resource_py3 import ApiManagementServiceResource
    from .apim_resource_py3 import ApimResource
    from .api_management_service_update_parameters_py3 import ApiManagementServiceUpdateParameters
    from .api_management_service_get_sso_token_result_py3 import ApiManagementServiceGetSsoTokenResult
    from .api_management_service_check_name_availability_parameters_py3 import ApiManagementServiceCheckNameAvailabilityParameters
    from .api_management_service_name_availability_result_py3 import ApiManagementServiceNameAvailabilityResult
    from .api_management_service_apply_network_configuration_parameters_py3 import ApiManagementServiceApplyNetworkConfigurationParameters
    from .operation_display_py3 import OperationDisplay
    from .operation_py3 import Operation
    from .email_template_parameters_contract_properties_py3 import EmailTemplateParametersContractProperties
    from .email_template_update_parameters_py3 import EmailTemplateUpdateParameters
    from .email_template_contract_py3 import EmailTemplateContract
    from .user_identity_contract_py3 import UserIdentityContract
    from .user_entity_base_parameters_py3 import UserEntityBaseParameters
    from .group_contract_properties_py3 import GroupContractProperties
    from .user_contract_py3 import UserContract
    from .group_update_parameters_py3 import GroupUpdateParameters
    from .group_contract_py3 import GroupContract
    from .group_create_parameters_py3 import GroupCreateParameters
    from .identity_provider_base_parameters_py3 import IdentityProviderBaseParameters
    from .identity_provider_update_parameters_py3 import IdentityProviderUpdateParameters
    from .identity_provider_contract_py3 import IdentityProviderContract
    from .logger_update_contract_py3 import LoggerUpdateContract
    from .logger_contract_py3 import LoggerContract
    from .connectivity_status_contract_py3 import ConnectivityStatusContract
    from .network_status_contract_py3 import NetworkStatusContract
    from .network_status_contract_by_location_py3 import NetworkStatusContractByLocation
    from .recipient_email_contract_py3 import RecipientEmailContract
    from .recipient_email_collection_py3 import RecipientEmailCollection
    from .recipient_user_contract_py3 import RecipientUserContract
    from .recipient_user_collection_py3 import RecipientUserCollection
    from .recipients_contract_properties_py3 import RecipientsContractProperties
    from .notification_contract_py3 import NotificationContract
    from .openid_connect_provider_update_contract_py3 import OpenidConnectProviderUpdateContract
    from .openid_connect_provider_contract_py3 import OpenidConnectProviderContract
    from .policy_snippet_contract_py3 import PolicySnippetContract
    from .policy_snippets_collection_py3 import PolicySnippetsCollection
    from .registration_delegation_settings_properties_py3 import RegistrationDelegationSettingsProperties
    from .subscriptions_delegation_settings_properties_py3 import SubscriptionsDelegationSettingsProperties
    from .portal_delegation_settings_py3 import PortalDelegationSettings
    from .terms_of_service_properties_py3 import TermsOfServiceProperties
    from .portal_signup_settings_py3 import PortalSignupSettings
    from .portal_signin_settings_py3 import PortalSigninSettings
    from .subscription_contract_py3 import SubscriptionContract
    from .product_update_parameters_py3 import ProductUpdateParameters
    from .property_entity_base_parameters_py3 import PropertyEntityBaseParameters
    from .property_update_parameters_py3 import PropertyUpdateParameters
    from .property_contract_py3 import PropertyContract
    from .quota_counter_value_contract_properties_py3 import QuotaCounterValueContractProperties
    from .quota_counter_contract_py3 import QuotaCounterContract
    from .quota_counter_collection_py3 import QuotaCounterCollection
    from .request_report_record_contract_py3 import RequestReportRecordContract
    from .report_record_contract_py3 import ReportRecordContract
    from .subscription_update_parameters_py3 import SubscriptionUpdateParameters
    from .subscription_create_parameters_py3 import SubscriptionCreateParameters
    from .tag_create_update_parameters_py3 import TagCreateUpdateParameters
    from .tenant_configuration_sync_state_contract_py3 import TenantConfigurationSyncStateContract
    from .operation_result_log_item_contract_py3 import OperationResultLogItemContract
    from .operation_result_contract_py3 import OperationResultContract
    from .deploy_configuration_parameters_py3 import DeployConfigurationParameters
    from .save_configuration_parameter_py3 import SaveConfigurationParameter
    from .access_information_contract_py3 import AccessInformationContract
    from .access_information_update_parameters_py3 import AccessInformationUpdateParameters
    from .user_token_result_py3 import UserTokenResult
    from .user_token_parameters_py3 import UserTokenParameters
    from .generate_sso_url_result_py3 import GenerateSsoUrlResult
    from .user_update_parameters_py3 import UserUpdateParameters
    from .user_create_parameters_py3 import UserCreateParameters
    from .api_revision_info_contract_py3 import ApiRevisionInfoContract
    from .quota_counter_value_contract_py3 import QuotaCounterValueContract
except (SyntaxError, ImportError):
    from .error_field_contract import ErrorFieldContract
    from .error_response_body import ErrorResponseBody
    from .error_response import ErrorResponse, ErrorResponseException
    from .region_contract import RegionContract
    from .resource import Resource
    from .api_export_result import ApiExportResult
    from .product_entity_base_parameters import ProductEntityBaseParameters
    from .product_tag_resource_contract_properties import ProductTagResourceContractProperties
    from .operation_tag_resource_contract_properties import OperationTagResourceContractProperties
    from .subscription_key_parameter_names_contract import SubscriptionKeyParameterNamesContract
    from .open_id_authentication_settings_contract import OpenIdAuthenticationSettingsContract
    from .oauth2_authentication_settings_contract import OAuth2AuthenticationSettingsContract
    from .authentication_settings_contract import AuthenticationSettingsContract
    from .api_version_set_contract_details import ApiVersionSetContractDetails
    from .api_create_or_update_properties_wsdl_selector import ApiCreateOrUpdatePropertiesWsdlSelector
    from .api_contract_properties import ApiContractProperties
    from .api_entity_base_contract import ApiEntityBaseContract
    from .api_tag_resource_contract_properties import ApiTagResourceContractProperties
    from .tag_tag_resource_contract_properties import TagTagResourceContractProperties
    from .tag_resource_contract import TagResourceContract
    from .tag_contract import TagContract
    from .tag_description_contract import TagDescriptionContract
    from .tag_description_create_parameters import TagDescriptionCreateParameters
    from .issue_attachment_contract import IssueAttachmentContract
    from .issue_comment_contract import IssueCommentContract
    from .issue_contract_base_properties import IssueContractBaseProperties
    from .issue_update_contract import IssueUpdateContract
    from .issue_contract import IssueContract
    from .body_diagnostic_settings import BodyDiagnosticSettings
    from .http_message_diagnostic import HttpMessageDiagnostic
    from .pipeline_diagnostic_settings import PipelineDiagnosticSettings
    from .sampling_settings import SamplingSettings
    from .diagnostic_contract import DiagnosticContract
    from .schema_contract import SchemaContract
    from .policy_contract import PolicyContract
    from .policy_collection import PolicyCollection
    from .product_contract import ProductContract
    from .parameter_contract import ParameterContract
    from .representation_contract import RepresentationContract
    from .response_contract import ResponseContract
    from .request_contract import RequestContract
    from .operation_entity_base_contract import OperationEntityBaseContract
    from .operation_update_contract import OperationUpdateContract
    from .operation_contract import OperationContract
    from .api_release_contract import ApiReleaseContract
    from .api_revision_contract import ApiRevisionContract
    from .api_update_contract import ApiUpdateContract
    from .api_contract import ApiContract
    from .api_create_or_update_parameter import ApiCreateOrUpdateParameter
    from .api_version_set_entity_base import ApiVersionSetEntityBase
    from .api_version_set_update_parameters import ApiVersionSetUpdateParameters
    from .api_version_set_contract import ApiVersionSetContract
    from .token_body_parameter_contract import TokenBodyParameterContract
    from .authorization_server_contract_base_properties import AuthorizationServerContractBaseProperties
    from .authorization_server_update_contract import AuthorizationServerUpdateContract
    from .authorization_server_contract import AuthorizationServerContract
    from .backend_reconnect_contract import BackendReconnectContract
    from .backend_tls_properties import BackendTlsProperties
    from .backend_proxy_contract import BackendProxyContract
    from .backend_authorization_header_credentials import BackendAuthorizationHeaderCredentials
    from .backend_credentials_contract import BackendCredentialsContract
    from .x509_certificate_name import X509CertificateName
    from .backend_service_fabric_cluster_properties import BackendServiceFabricClusterProperties
    from .backend_properties import BackendProperties
    from .backend_base_parameters import BackendBaseParameters
    from .backend_update_parameters import BackendUpdateParameters
    from .backend_contract import BackendContract
    from .cache_update_parameters import CacheUpdateParameters
    from .cache_contract import CacheContract
    from .certificate_contract import CertificateContract
    from .certificate_create_or_update_parameters import CertificateCreateOrUpdateParameters
    from .resource_sku import ResourceSku
    from .resource_sku_capacity import ResourceSkuCapacity
    from .resource_sku_result import ResourceSkuResult
    from .certificate_information import CertificateInformation
    from .certificate_configuration import CertificateConfiguration
    from .hostname_configuration import HostnameConfiguration
    from .virtual_network_configuration import VirtualNetworkConfiguration
    from .api_management_service_sku_properties import ApiManagementServiceSkuProperties
    from .additional_location import AdditionalLocation
    from .api_management_service_backup_restore_parameters import ApiManagementServiceBackupRestoreParameters
    from .api_management_service_base_properties import ApiManagementServiceBaseProperties
    from .api_management_service_identity import ApiManagementServiceIdentity
    from .api_management_service_resource import ApiManagementServiceResource
    from .apim_resource import ApimResource
    from .api_management_service_update_parameters import ApiManagementServiceUpdateParameters
    from .api_management_service_get_sso_token_result import ApiManagementServiceGetSsoTokenResult
    from .api_management_service_check_name_availability_parameters import ApiManagementServiceCheckNameAvailabilityParameters
    from .api_management_service_name_availability_result import ApiManagementServiceNameAvailabilityResult
    from .api_management_service_apply_network_configuration_parameters import ApiManagementServiceApplyNetworkConfigurationParameters
    from .operation_display import OperationDisplay
    from .operation import Operation
    from .email_template_parameters_contract_properties import EmailTemplateParametersContractProperties
    from .email_template_update_parameters import EmailTemplateUpdateParameters
    from .email_template_contract import EmailTemplateContract
    from .user_identity_contract import UserIdentityContract
    from .user_entity_base_parameters import UserEntityBaseParameters
    from .group_contract_properties import GroupContractProperties
    from .user_contract import UserContract
    from .group_update_parameters import GroupUpdateParameters
    from .group_contract import GroupContract
    from .group_create_parameters import GroupCreateParameters
    from .identity_provider_base_parameters import IdentityProviderBaseParameters
    from .identity_provider_update_parameters import IdentityProviderUpdateParameters
    from .identity_provider_contract import IdentityProviderContract
    from .logger_update_contract import LoggerUpdateContract
    from .logger_contract import LoggerContract
    from .connectivity_status_contract import ConnectivityStatusContract
    from .network_status_contract import NetworkStatusContract
    from .network_status_contract_by_location import NetworkStatusContractByLocation
    from .recipient_email_contract import RecipientEmailContract
    from .recipient_email_collection import RecipientEmailCollection
    from .recipient_user_contract import RecipientUserContract
    from .recipient_user_collection import RecipientUserCollection
    from .recipients_contract_properties import RecipientsContractProperties
    from .notification_contract import NotificationContract
    from .openid_connect_provider_update_contract import OpenidConnectProviderUpdateContract
    from .openid_connect_provider_contract import OpenidConnectProviderContract
    from .policy_snippet_contract import PolicySnippetContract
    from .policy_snippets_collection import PolicySnippetsCollection
    from .registration_delegation_settings_properties import RegistrationDelegationSettingsProperties
    from .subscriptions_delegation_settings_properties import SubscriptionsDelegationSettingsProperties
    from .portal_delegation_settings import PortalDelegationSettings
    from .terms_of_service_properties import TermsOfServiceProperties
    from .portal_signup_settings import PortalSignupSettings
    from .portal_signin_settings import PortalSigninSettings
    from .subscription_contract import SubscriptionContract
    from .product_update_parameters import ProductUpdateParameters
    from .property_entity_base_parameters import PropertyEntityBaseParameters
    from .property_update_parameters import PropertyUpdateParameters
    from .property_contract import PropertyContract
    from .quota_counter_value_contract_properties import QuotaCounterValueContractProperties
    from .quota_counter_contract import QuotaCounterContract
    from .quota_counter_collection import QuotaCounterCollection
    from .request_report_record_contract import RequestReportRecordContract
    from .report_record_contract import ReportRecordContract
    from .subscription_update_parameters import SubscriptionUpdateParameters
    from .subscription_create_parameters import SubscriptionCreateParameters
    from .tag_create_update_parameters import TagCreateUpdateParameters
    from .tenant_configuration_sync_state_contract import TenantConfigurationSyncStateContract
    from .operation_result_log_item_contract import OperationResultLogItemContract
    from .operation_result_contract import OperationResultContract
    from .deploy_configuration_parameters import DeployConfigurationParameters
    from .save_configuration_parameter import SaveConfigurationParameter
    from .access_information_contract import AccessInformationContract
    from .access_information_update_parameters import AccessInformationUpdateParameters
    from .user_token_result import UserTokenResult
    from .user_token_parameters import UserTokenParameters
    from .generate_sso_url_result import GenerateSsoUrlResult
    from .user_update_parameters import UserUpdateParameters
    from .user_create_parameters import UserCreateParameters
    from .api_revision_info_contract import ApiRevisionInfoContract
    from .quota_counter_value_contract import QuotaCounterValueContract
from .api_contract_paged import ApiContractPaged
from .tag_resource_contract_paged import TagResourceContractPaged
from .api_revision_contract_paged import ApiRevisionContractPaged
from .api_release_contract_paged import ApiReleaseContractPaged
from .operation_contract_paged import OperationContractPaged
from .tag_contract_paged import TagContractPaged
from .product_contract_paged import ProductContractPaged
from .schema_contract_paged import SchemaContractPaged
from .diagnostic_contract_paged import DiagnosticContractPaged
from .issue_contract_paged import IssueContractPaged
from .issue_comment_contract_paged import IssueCommentContractPaged
from .issue_attachment_contract_paged import IssueAttachmentContractPaged
from .tag_description_contract_paged import TagDescriptionContractPaged
from .api_version_set_contract_paged import ApiVersionSetContractPaged
from .authorization_server_contract_paged import AuthorizationServerContractPaged
from .backend_contract_paged import BackendContractPaged
from .cache_contract_paged import CacheContractPaged
from .certificate_contract_paged import CertificateContractPaged
from .operation_paged import OperationPaged
from .resource_sku_result_paged import ResourceSkuResultPaged
from .api_management_service_resource_paged import ApiManagementServiceResourcePaged
from .email_template_contract_paged import EmailTemplateContractPaged
from .group_contract_paged import GroupContractPaged
from .user_contract_paged import UserContractPaged
from .identity_provider_contract_paged import IdentityProviderContractPaged
from .logger_contract_paged import LoggerContractPaged
from .notification_contract_paged import NotificationContractPaged
from .openid_connect_provider_contract_paged import OpenidConnectProviderContractPaged
from .subscription_contract_paged import SubscriptionContractPaged
from .property_contract_paged import PropertyContractPaged
from .region_contract_paged import RegionContractPaged
from .report_record_contract_paged import ReportRecordContractPaged
from .request_report_record_contract_paged import RequestReportRecordContractPaged
from .user_identity_contract_paged import UserIdentityContractPaged
from .api_management_client_enums import (
    ProductState,
    BearerTokenSendingMethods,
    Protocol,
    ContentFormat,
    SoapApiType,
    ApiType,
    State,
    SamplingType,
    AlwaysLog,
    PolicyContentFormat,
    VersioningScheme,
    GrantType,
    AuthorizationMethod,
    ClientAuthenticationMethod,
    BearerTokenSendingMethod,
    BackendProtocol,
    SkuType,
    ResourceSkuCapacityScaleType,
    HostnameType,
    VirtualNetworkType,
    NameAvailabilityReason,
    Confirmation,
    UserState,
    GroupType,
    IdentityProviderType,
    LoggerType,
    ConnectivityStatusType,
    SubscriptionState,
    AsyncOperationStatus,
    KeyType,
    NotificationName,
    TemplateName,
    PolicyScopeContract,
    ExportFormat,
)

__all__ = [
    'ErrorFieldContract',
    'ErrorResponseBody',
    'ErrorResponse', 'ErrorResponseException',
    'RegionContract',
    'Resource',
    'ApiExportResult',
    'ProductEntityBaseParameters',
    'ProductTagResourceContractProperties',
    'OperationTagResourceContractProperties',
    'SubscriptionKeyParameterNamesContract',
    'OpenIdAuthenticationSettingsContract',
    'OAuth2AuthenticationSettingsContract',
    'AuthenticationSettingsContract',
    'ApiVersionSetContractDetails',
    'ApiCreateOrUpdatePropertiesWsdlSelector',
    'ApiContractProperties',
    'ApiEntityBaseContract',
    'ApiTagResourceContractProperties',
    'TagTagResourceContractProperties',
    'TagResourceContract',
    'TagContract',
    'TagDescriptionContract',
    'TagDescriptionCreateParameters',
    'IssueAttachmentContract',
    'IssueCommentContract',
    'IssueContractBaseProperties',
    'IssueUpdateContract',
    'IssueContract',
    'BodyDiagnosticSettings',
    'HttpMessageDiagnostic',
    'PipelineDiagnosticSettings',
    'SamplingSettings',
    'DiagnosticContract',
    'SchemaContract',
    'PolicyContract',
    'PolicyCollection',
    'ProductContract',
    'ParameterContract',
    'RepresentationContract',
    'ResponseContract',
    'RequestContract',
    'OperationEntityBaseContract',
    'OperationUpdateContract',
    'OperationContract',
    'ApiReleaseContract',
    'ApiRevisionContract',
    'ApiUpdateContract',
    'ApiContract',
    'ApiCreateOrUpdateParameter',
    'ApiVersionSetEntityBase',
    'ApiVersionSetUpdateParameters',
    'ApiVersionSetContract',
    'TokenBodyParameterContract',
    'AuthorizationServerContractBaseProperties',
    'AuthorizationServerUpdateContract',
    'AuthorizationServerContract',
    'BackendReconnectContract',
    'BackendTlsProperties',
    'BackendProxyContract',
    'BackendAuthorizationHeaderCredentials',
    'BackendCredentialsContract',
    'X509CertificateName',
    'BackendServiceFabricClusterProperties',
    'BackendProperties',
    'BackendBaseParameters',
    'BackendUpdateParameters',
    'BackendContract',
    'CacheUpdateParameters',
    'CacheContract',
    'CertificateContract',
    'CertificateCreateOrUpdateParameters',
    'ResourceSku',
    'ResourceSkuCapacity',
    'ResourceSkuResult',
    'CertificateInformation',
    'CertificateConfiguration',
    'HostnameConfiguration',
    'VirtualNetworkConfiguration',
    'ApiManagementServiceSkuProperties',
    'AdditionalLocation',
    'ApiManagementServiceBackupRestoreParameters',
    'ApiManagementServiceBaseProperties',
    'ApiManagementServiceIdentity',
    'ApiManagementServiceResource',
    'ApimResource',
    'ApiManagementServiceUpdateParameters',
    'ApiManagementServiceGetSsoTokenResult',
    'ApiManagementServiceCheckNameAvailabilityParameters',
    'ApiManagementServiceNameAvailabilityResult',
    'ApiManagementServiceApplyNetworkConfigurationParameters',
    'OperationDisplay',
    'Operation',
    'EmailTemplateParametersContractProperties',
    'EmailTemplateUpdateParameters',
    'EmailTemplateContract',
    'UserIdentityContract',
    'UserEntityBaseParameters',
    'GroupContractProperties',
    'UserContract',
    'GroupUpdateParameters',
    'GroupContract',
    'GroupCreateParameters',
    'IdentityProviderBaseParameters',
    'IdentityProviderUpdateParameters',
    'IdentityProviderContract',
    'LoggerUpdateContract',
    'LoggerContract',
    'ConnectivityStatusContract',
    'NetworkStatusContract',
    'NetworkStatusContractByLocation',
    'RecipientEmailContract',
    'RecipientEmailCollection',
    'RecipientUserContract',
    'RecipientUserCollection',
    'RecipientsContractProperties',
    'NotificationContract',
    'OpenidConnectProviderUpdateContract',
    'OpenidConnectProviderContract',
    'PolicySnippetContract',
    'PolicySnippetsCollection',
    'RegistrationDelegationSettingsProperties',
    'SubscriptionsDelegationSettingsProperties',
    'PortalDelegationSettings',
    'TermsOfServiceProperties',
    'PortalSignupSettings',
    'PortalSigninSettings',
    'SubscriptionContract',
    'ProductUpdateParameters',
    'PropertyEntityBaseParameters',
    'PropertyUpdateParameters',
    'PropertyContract',
    'QuotaCounterValueContractProperties',
    'QuotaCounterContract',
    'QuotaCounterCollection',
    'RequestReportRecordContract',
    'ReportRecordContract',
    'SubscriptionUpdateParameters',
    'SubscriptionCreateParameters',
    'TagCreateUpdateParameters',
    'TenantConfigurationSyncStateContract',
    'OperationResultLogItemContract',
    'OperationResultContract',
    'DeployConfigurationParameters',
    'SaveConfigurationParameter',
    'AccessInformationContract',
    'AccessInformationUpdateParameters',
    'UserTokenResult',
    'UserTokenParameters',
    'GenerateSsoUrlResult',
    'UserUpdateParameters',
    'UserCreateParameters',
    'ApiRevisionInfoContract',
    'QuotaCounterValueContract',
    'ApiContractPaged',
    'TagResourceContractPaged',
    'ApiRevisionContractPaged',
    'ApiReleaseContractPaged',
    'OperationContractPaged',
    'TagContractPaged',
    'ProductContractPaged',
    'SchemaContractPaged',
    'DiagnosticContractPaged',
    'IssueContractPaged',
    'IssueCommentContractPaged',
    'IssueAttachmentContractPaged',
    'TagDescriptionContractPaged',
    'ApiVersionSetContractPaged',
    'AuthorizationServerContractPaged',
    'BackendContractPaged',
    'CacheContractPaged',
    'CertificateContractPaged',
    'OperationPaged',
    'ResourceSkuResultPaged',
    'ApiManagementServiceResourcePaged',
    'EmailTemplateContractPaged',
    'GroupContractPaged',
    'UserContractPaged',
    'IdentityProviderContractPaged',
    'LoggerContractPaged',
    'NotificationContractPaged',
    'OpenidConnectProviderContractPaged',
    'SubscriptionContractPaged',
    'PropertyContractPaged',
    'RegionContractPaged',
    'ReportRecordContractPaged',
    'RequestReportRecordContractPaged',
    'UserIdentityContractPaged',
    'ProductState',
    'BearerTokenSendingMethods',
    'Protocol',
    'ContentFormat',
    'SoapApiType',
    'ApiType',
    'State',
    'SamplingType',
    'AlwaysLog',
    'PolicyContentFormat',
    'VersioningScheme',
    'GrantType',
    'AuthorizationMethod',
    'ClientAuthenticationMethod',
    'BearerTokenSendingMethod',
    'BackendProtocol',
    'SkuType',
    'ResourceSkuCapacityScaleType',
    'HostnameType',
    'VirtualNetworkType',
    'NameAvailabilityReason',
    'Confirmation',
    'UserState',
    'GroupType',
    'IdentityProviderType',
    'LoggerType',
    'ConnectivityStatusType',
    'SubscriptionState',
    'AsyncOperationStatus',
    'KeyType',
    'NotificationName',
    'TemplateName',
    'PolicyScopeContract',
    'ExportFormat',
]
