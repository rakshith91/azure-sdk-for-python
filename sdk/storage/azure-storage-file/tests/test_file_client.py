# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import unittest
import platform

from azure.core.exceptions import AzureError
from devtools_testutils import ResourceGroupPreparer, StorageAccountPreparer
from azure.storage.file import (
    VERSION,
    FileServiceClient,
    ShareClient,
    DirectoryClient,
    FileClient)

from filetestcase import (
    FileTestCase
)
#from azure.storage.common import TokenCredential

# ------------------------------------------------------------------------------

SERVICES = {
    FileServiceClient: 'file',
    ShareClient: 'file',
    DirectoryClient: 'file',
    FileClient: 'file',
}

_CONNECTION_ENDPOINTS = {'file': 'FileEndpoint'}

_CONNECTION_ENDPOINTS_SECONDARY = {'file': 'FileSecondaryEndpoint'}

class StorageFileClientTest(FileTestCase):
    def setUp(self):
        super(StorageFileClientTest, self).setUp()
        self.sas_token = '?sv=2015-04-05&st=2015-04-29T22%3A18%3A26Z&se=2015-04-30T02%3A23%3A26Z&sr=b&sp=rw&sip=168.1.5.60-168.1.5.70&spr=https&sig=Z%2FRHIX5Xcg0Mq2rqI3OlWTjEg2tYkboXr1P9ZUXDtkk%3D'
        self.token_credential = self.generate_oauth_token()

    # --Helpers-----------------------------------------------------------------
    def validate_standard_account_endpoints(self, service, service_type, account_name, key, protocol='https'):
        self.assertIsNotNone(service)
        self.assertEqual(service.credential.account_name, account_name)
        self.assertEqual(service.credential.account_key, key)
        self.assertTrue(service.primary_endpoint.startswith('{}://{}.{}.core.windows.net/'.format(
            protocol, account_name, service_type)))
        self.assertTrue(service.secondary_endpoint.startswith('{}://{}-secondary.{}.core.windows.net/'.format(
            protocol, account_name, service_type)))

    # --Direct Parameters Test Cases --------------------------------------------
    @ResourceGroupPreparer()          
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    def test_create_service_with_key(self, resource_group, location, storage_account, storage_account_key):
        # Arrange

        for client, url in SERVICES.items():
            # Act
            service = client(
                self._account_url(storage_account.name), credential=storage_account_key,
                share='foo', directory_path='bar', file_path='baz')

            # Assert
            self.validate_standard_account_endpoints(service, url, storage_account.name, storage_account_key)
            self.assertEqual(service.scheme, 'https')

    @ResourceGroupPreparer()          
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    def test_create_service_with_sas(self, resource_group, location, storage_account, storage_account_key):
        # Arrange

        for service_type in SERVICES:
            # Act
            service = service_type(
                self._account_url(storage_account.name), credential=self.sas_token,
                share='foo', directory_path='bar', file_path='baz')

            # Assert
            self.assertIsNotNone(service)
            self.assertIsNone(service.credential)
            self.assertTrue(service.url.endswith(self.sas_token))

    @ResourceGroupPreparer()          
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    def test_create_service_with_token(self, resource_group, location, storage_account, storage_account_key):
        for service_type in SERVICES:
            # Act
            # token credential is not available for FileService
            with self.assertRaises(ValueError):
                service_type(self._account_url(storage_account.name), credential=self.token_credential,
                             share='foo', directory_path='bar', file_path='baz')

    @ResourceGroupPreparer()          
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    def test_create_service_china(self, resource_group, location, storage_account, storage_account_key):
        # Arrange
        url = self._account_url(storage_account.name).replace('core.windows.net', 'core.chinacloudapi.cn')
        for service_type in SERVICES.items():
            # Act
            service = service_type[0](
                url, credential=storage_account_key,
                share='foo', directory_path='bar', file_path='baz')

            # Assert
            self.assertIsNotNone(service)
            self.assertEqual(service.credential.account_name, storage_account.name)
            self.assertEqual(service.credential.account_key, storage_account_key)
            self.assertEqual(service.primary_hostname, '{}.{}.core.chinacloudapi.cn'.format(
                storage_account.name, service_type[1]))
            self.assertEqual(service.secondary_hostname,
                             '{}-secondary.{}.core.chinacloudapi.cn'.format(storage_account.name, service_type[1]))

    @ResourceGroupPreparer()          
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    def test_create_service_protocol(self, resource_group, location, storage_account, storage_account_key):
        # Arrange
        url = self._account_url(storage_account.name).replace('https', 'http')
        for service_type in SERVICES.items():
            # Act
            service = service_type[0](
                url, credential=storage_account_key, share='foo', directory_path='bar', file_path='baz')

            # Assert
            self.validate_standard_account_endpoints(service, service_type[1], storage_account.name, storage_account_key,  protocol='http')
            self.assertEqual(service.scheme, 'http')

    @ResourceGroupPreparer()          
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    def test_create_service_empty_key(self, resource_group, location, storage_account, storage_account_key):
        # Arrange
        for service_type in SERVICES:
            # Act
            # Passing an empty key to create account should fail.
            with self.assertRaises(ValueError) as e:
                service_type(
                    self._account_url(storage_account.name), share='foo', directory_path='bar', file_path='baz')

            self.assertEqual(
                str(e.exception),
                'You need to provide either an account key or SAS token when creating a storage service.')

    @ResourceGroupPreparer()          
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    def test_create_service_missing_arguments(self, resource_group, location, storage_account, storage_account_key):
        # Arrange

        for service_type in SERVICES:
            # Act
            with self.assertRaises(ValueError):
                service_type(None)

    @ResourceGroupPreparer()          
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    def test_create_service_with_socket_timeout(self, resource_group, location, storage_account, storage_account_key):
        # Arrange

        for service_type in SERVICES.items():
            # Act
            default_service = service_type[0](
                self._account_url(storage_account.name), credential=storage_account_key,
                share='foo', directory_path='bar', file_path='baz')
            service = service_type[0](
                self._account_url(storage_account.name), credential=storage_account_key, connection_timeout=22,
                share='foo', directory_path='bar', file_path='baz')

            # Assert
            self.validate_standard_account_endpoints(service, service_type[1], storage_account.name, storage_account_key)
            assert service._client._client._pipeline._transport.connection_config.timeout == 22
            assert default_service._client._client._pipeline._transport.connection_config.timeout in [20, (20, 2000)]

    # --Connection String Test Cases --------------------------------------------
    @ResourceGroupPreparer()          
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    def test_create_service_with_connection_string_key(self, resource_group, location, storage_account, storage_account_key):
        # Arrange
        conn_string = 'AccountName={};AccountKey={};'.format(storage_account.name, storage_account_key)

        for service_type in SERVICES.items():
            # Act
            service = service_type[0].from_connection_string(
                conn_string, share='foo', directory_path='bar', file_path='baz')

            # Assert
            self.validate_standard_account_endpoints(service, service_type[1], storage_account.name, storage_account_key)
            self.assertEqual(service.scheme, 'https')

    @ResourceGroupPreparer()          
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    def test_create_service_with_connection_string_sas(self, resource_group, location, storage_account, storage_account_key):
        # Arrange
        conn_string = 'AccountName={};SharedAccessSignature={};'.format(storage_account.name, self.sas_token)

        for service_type in SERVICES.items():
            # Act
            service = service_type[0].from_connection_string(
                conn_string, share='foo', directory_path='bar', file_path='baz')

            # Assert
            self.assertIsNotNone(service)
            self.assertIsNone(service.credential)
            self.assertTrue(service.url.endswith(self.sas_token))

    @ResourceGroupPreparer()          
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    def test_create_service_with_connection_string_endpoint_protocol(self, resource_group, location, storage_account, storage_account_key):
        # Arrange
        conn_string = 'AccountName={};AccountKey={};DefaultEndpointsProtocol=http;EndpointSuffix=core.chinacloudapi.cn;'.format(
            storage_account.name, storage_account_key)

        for service_type in SERVICES.items():
            # Act
            service = service_type[0].from_connection_string(
                conn_string, share='foo', directory_path='bar', file_path='baz')

            # Assert
            self.assertIsNotNone(service)
            self.assertEqual(service.credential.account_name, storage_account.name)
            self.assertEqual(service.credential.account_key, storage_account_key)
            self.assertEqual(service.primary_hostname, '{}.{}.core.chinacloudapi.cn'.format(storage_account.name, service_type[1]))
            self.assertEqual(service.secondary_hostname,
                             '{}-secondary.{}.core.chinacloudapi.cn'.format(storage_account.name, service_type[1]))
            self.assertEqual(service.scheme, 'http')

    @ResourceGroupPreparer()          
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    def test_create_service_with_connection_string_emulated(self, resource_group, location, storage_account, storage_account_key):
        # Arrange
        for service_type in SERVICES.items():
            conn_string = 'UseDevelopmentStorage=true;'

            # Act
            with self.assertRaises(ValueError):
                service_type[0].from_connection_string(
                    conn_string, share='foo', directory_path='bar', file_path='baz')

    @ResourceGroupPreparer()          
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    def test_create_service_with_conn_str_fails_if_sec_without_prim(self, resource_group, location, storage_account, storage_account_key):
        for service_type in SERVICES.items():
            # Arrange
            conn_string = 'AccountName={};AccountKey={};{}=www.mydomain.com;'.format(
                storage_account.name, storage_account_key, _CONNECTION_ENDPOINTS_SECONDARY.get(service_type[1]))

            # Act

            # Fails if primary excluded
            with self.assertRaises(ValueError):
                service_type[0].from_connection_string(
                    conn_string, share='foo', directory_path='bar', file_path='baz')

    @ResourceGroupPreparer()          
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    def test_create_service_with_conn_str_succeeds_if_sec_with_prim(self, resource_group, location, storage_account, storage_account_key):
        for service_type in SERVICES.items():
            # Arrange
            conn_string = 'AccountName={};AccountKey={};{}=www.mydomain.com;{}=www-sec.mydomain.com;'.format(
                storage_account.name, storage_account_key,
                _CONNECTION_ENDPOINTS.get(service_type[1]),
                _CONNECTION_ENDPOINTS_SECONDARY.get(service_type[1]))

            # Act
            service = service_type[0].from_connection_string(
                conn_string, share='foo', directory_path='bar', file_path='baz')

            # Assert
            self.assertIsNotNone(service)
            self.assertEqual(service.credential.account_name, storage_account.name)
            self.assertEqual(service.credential.account_key, storage_account_key)
            self.assertEqual(service.primary_hostname, 'www.mydomain.com')
            self.assertEqual(service.secondary_hostname, 'www-sec.mydomain.com')

    @ResourceGroupPreparer()          
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    def test_client_request_id_echo(self, resource_group, location, storage_account, storage_account_key):
        # client request id is different for every request, so it will never match the recorded one
        if not self.is_live:
            return

        # Arrange
        service = FileServiceClient(self._account_url(storage_account.name), credential=storage_account_key)
        request_id_header_name = 'x-ms-client-request-id'

        # Act make the client request ID slightly different
        def callback(response):
            response.http_response.status_code = 200
            response.http_response.headers[request_id_header_name] += '1'

        # Assert the client request ID validation is working
        with self.assertRaises(AzureError):
            service.get_service_properties(raw_response_hook=callback)

        # Act remove the echoed client request ID
        def callback(response):
            response.status_code = 200
            del response.http_response.headers[request_id_header_name]

        # Assert the client request ID validation is not throwing when the ID is not echoed
        service.get_service_properties(raw_response_hook=callback)

    @ResourceGroupPreparer()          
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    def test_user_agent_default(self, resource_group, location, storage_account, storage_account_key):
        service = FileServiceClient(self._account_url(storage_account.name), credential=storage_account_key)

        def callback(response):
            self.assertTrue('User-Agent' in response.http_request.headers)
            self.assertEqual(
                response.http_request.headers['User-Agent'],
                "azsdk-python-storage-file/{} Python/{} ({})".format(
                    VERSION,
                    platform.python_version(),
                    platform.platform()))

        service.get_service_properties(raw_response_hook=callback)

    @ResourceGroupPreparer()          
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    def test_user_agent_custom(self, resource_group, location, storage_account, storage_account_key):
        custom_app = "TestApp/v1.0"
        service = FileServiceClient(
            self._account_url(storage_account.name), credential=storage_account_key, user_agent=custom_app)

        def callback1(response):
            self.assertTrue('User-Agent' in response.http_request.headers)
            self.assertEqual(
                response.http_request.headers['User-Agent'],
                "TestApp/v1.0 azsdk-python-storage-file/{} Python/{} ({})".format(
                    VERSION,
                    platform.python_version(),
                    platform.platform()))

        service.get_service_properties(raw_response_hook=callback1)

        def callback2(response):
            self.assertTrue('User-Agent' in response.http_request.headers)
            self.assertEqual(
                response.http_request.headers['User-Agent'],
                "TestApp/v2.0 azsdk-python-storage-file/{} Python/{} ({})".format(
                    VERSION,
                    platform.python_version(),
                    platform.platform()))

        service.get_service_properties(raw_response_hook=callback2, user_agent="TestApp/v2.0")

    @ResourceGroupPreparer()          
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    def test_user_agent_append(self, resource_group, location, storage_account, storage_account_key):
        service = FileServiceClient(self._account_url(storage_account.name), credential=storage_account_key)

        def callback(response):
            self.assertTrue('User-Agent' in response.http_request.headers)
            self.assertEqual(
                response.http_request.headers['User-Agent'],
                "azsdk-python-storage-file/{} Python/{} ({}) customer_user_agent".format(
                    VERSION,
                    platform.python_version(),
                    platform.platform()))

        custom_headers = {'User-Agent': 'customer_user_agent'}
        service.get_service_properties(raw_response_hook=callback, headers=custom_headers)


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
