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

import uuid
from msrest.pipeline import ClientRawResponse
from msrestazure.azure_exceptions import CloudError

from .. import models


class DenyAssignmentsOperations(object):
    """DenyAssignmentsOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: The API version to use for this operation. Constant value: "2018-07-01-preview".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2018-07-01-preview"

        self.config = config

    def list_for_resource(
            self, resource_group_name, resource_provider_namespace, parent_resource_path, resource_type, resource_name, filter=None, custom_headers=None, raw=False, **operation_config):
        """Gets deny assignments for a resource.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param resource_provider_namespace: The namespace of the resource
         provider.
        :type resource_provider_namespace: str
        :param parent_resource_path: The parent resource identity.
        :type parent_resource_path: str
        :param resource_type: The resource type of the resource.
        :type resource_type: str
        :param resource_name: The name of the resource to get deny assignments
         for.
        :type resource_name: str
        :param filter: The filter to apply on the operation. Use
         $filter=atScope() to return all deny assignments at or above the
         scope. Use $filter=denyAssignmentName eq '{name}' to search deny
         assignments by name at specified scope. Use $filter=principalId eq
         '{id}' to return all deny assignments at, above and below the scope
         for the specified principal. Use $filter=gdprExportPrincipalId eq
         '{id}' to return all deny assignments at, above and below the scope
         for the specified principal. This filter is different from the
         principalId filter as it returns not only those deny assignments that
         contain the specified principal is the Principals list but also those
         deny assignments that contain the specified principal is the
         ExcludePrincipals list. Additionally, when gdprExportPrincipalId
         filter is used, only the deny assignment name and description
         properties are returned.
        :type filter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of DenyAssignment
        :rtype:
         ~azure.mgmt.authorization.v2018_07_01_preview.models.DenyAssignmentPaged[~azure.mgmt.authorization.v2018_07_01_preview.models.DenyAssignment]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_for_resource.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                    'resourceProviderNamespace': self._serialize.url("resource_provider_namespace", resource_provider_namespace, 'str'),
                    'parentResourcePath': self._serialize.url("parent_resource_path", parent_resource_path, 'str', skip_quote=True),
                    'resourceType': self._serialize.url("resource_type", resource_type, 'str', skip_quote=True),
                    'resourceName': self._serialize.url("resource_name", resource_name, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
                if filter is not None:
                    query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def internal_paging(next_link=None):
            request = prepare_request(next_link)

            response = self._client.send(request, stream=False, **operation_config)

            if response.status_code not in [200]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            return response

        # Deserialize response
        header_dict = None
        if raw:
            header_dict = {}
        deserialized = models.DenyAssignmentPaged(internal_paging, self._deserialize.dependencies, header_dict)

        return deserialized
    list_for_resource.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePath}/{resourceType}/{resourceName}/providers/Microsoft.Authorization/denyAssignments'}

    def list_for_resource_group(
            self, resource_group_name, filter=None, custom_headers=None, raw=False, **operation_config):
        """Gets deny assignments for a resource group.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param filter: The filter to apply on the operation. Use
         $filter=atScope() to return all deny assignments at or above the
         scope. Use $filter=denyAssignmentName eq '{name}' to search deny
         assignments by name at specified scope. Use $filter=principalId eq
         '{id}' to return all deny assignments at, above and below the scope
         for the specified principal. Use $filter=gdprExportPrincipalId eq
         '{id}' to return all deny assignments at, above and below the scope
         for the specified principal. This filter is different from the
         principalId filter as it returns not only those deny assignments that
         contain the specified principal is the Principals list but also those
         deny assignments that contain the specified principal is the
         ExcludePrincipals list. Additionally, when gdprExportPrincipalId
         filter is used, only the deny assignment name and description
         properties are returned.
        :type filter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of DenyAssignment
        :rtype:
         ~azure.mgmt.authorization.v2018_07_01_preview.models.DenyAssignmentPaged[~azure.mgmt.authorization.v2018_07_01_preview.models.DenyAssignment]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_for_resource_group.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
                if filter is not None:
                    query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def internal_paging(next_link=None):
            request = prepare_request(next_link)

            response = self._client.send(request, stream=False, **operation_config)

            if response.status_code not in [200]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            return response

        # Deserialize response
        header_dict = None
        if raw:
            header_dict = {}
        deserialized = models.DenyAssignmentPaged(internal_paging, self._deserialize.dependencies, header_dict)

        return deserialized
    list_for_resource_group.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Authorization/denyAssignments'}

    def list(
            self, filter=None, custom_headers=None, raw=False, **operation_config):
        """Gets all deny assignments for the subscription.

        :param filter: The filter to apply on the operation. Use
         $filter=atScope() to return all deny assignments at or above the
         scope. Use $filter=denyAssignmentName eq '{name}' to search deny
         assignments by name at specified scope. Use $filter=principalId eq
         '{id}' to return all deny assignments at, above and below the scope
         for the specified principal. Use $filter=gdprExportPrincipalId eq
         '{id}' to return all deny assignments at, above and below the scope
         for the specified principal. This filter is different from the
         principalId filter as it returns not only those deny assignments that
         contain the specified principal is the Principals list but also those
         deny assignments that contain the specified principal is the
         ExcludePrincipals list. Additionally, when gdprExportPrincipalId
         filter is used, only the deny assignment name and description
         properties are returned.
        :type filter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of DenyAssignment
        :rtype:
         ~azure.mgmt.authorization.v2018_07_01_preview.models.DenyAssignmentPaged[~azure.mgmt.authorization.v2018_07_01_preview.models.DenyAssignment]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
                if filter is not None:
                    query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def internal_paging(next_link=None):
            request = prepare_request(next_link)

            response = self._client.send(request, stream=False, **operation_config)

            if response.status_code not in [200]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            return response

        # Deserialize response
        header_dict = None
        if raw:
            header_dict = {}
        deserialized = models.DenyAssignmentPaged(internal_paging, self._deserialize.dependencies, header_dict)

        return deserialized
    list.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/denyAssignments'}

    def get(
            self, scope, deny_assignment_id, custom_headers=None, raw=False, **operation_config):
        """Get the specified deny assignment.

        :param scope: The scope of the deny assignment.
        :type scope: str
        :param deny_assignment_id: The ID of the deny assignment to get.
        :type deny_assignment_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: DenyAssignment or ClientRawResponse if raw=true
        :rtype:
         ~azure.mgmt.authorization.v2018_07_01_preview.models.DenyAssignment or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str', skip_quote=True),
            'denyAssignmentId': self._serialize.url("deny_assignment_id", deny_assignment_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('DenyAssignment', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/{scope}/providers/Microsoft.Authorization/denyAssignments/{denyAssignmentId}'}

    def get_by_id(
            self, deny_assignment_id, custom_headers=None, raw=False, **operation_config):
        """Gets a deny assignment by ID.

        :param deny_assignment_id: The fully qualified deny assignment ID. For
         example, use the format,
         /subscriptions/{guid}/providers/Microsoft.Authorization/denyAssignments/{denyAssignmentId}
         for subscription level deny assignments, or
         /providers/Microsoft.Authorization/denyAssignments/{denyAssignmentId}
         for tenant level deny assignments.
        :type deny_assignment_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: DenyAssignment or ClientRawResponse if raw=true
        :rtype:
         ~azure.mgmt.authorization.v2018_07_01_preview.models.DenyAssignment or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        # Construct URL
        url = self.get_by_id.metadata['url']
        path_format_arguments = {
            'denyAssignmentId': self._serialize.url("deny_assignment_id", deny_assignment_id, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('DenyAssignment', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_by_id.metadata = {'url': '/{denyAssignmentId}'}

    def list_for_scope(
            self, scope, filter=None, custom_headers=None, raw=False, **operation_config):
        """Gets deny assignments for a scope.

        :param scope: The scope of the deny assignments.
        :type scope: str
        :param filter: The filter to apply on the operation. Use
         $filter=atScope() to return all deny assignments at or above the
         scope. Use $filter=denyAssignmentName eq '{name}' to search deny
         assignments by name at specified scope. Use $filter=principalId eq
         '{id}' to return all deny assignments at, above and below the scope
         for the specified principal. Use $filter=gdprExportPrincipalId eq
         '{id}' to return all deny assignments at, above and below the scope
         for the specified principal. This filter is different from the
         principalId filter as it returns not only those deny assignments that
         contain the specified principal is the Principals list but also those
         deny assignments that contain the specified principal is the
         ExcludePrincipals list. Additionally, when gdprExportPrincipalId
         filter is used, only the deny assignment name and description
         properties are returned.
        :type filter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of DenyAssignment
        :rtype:
         ~azure.mgmt.authorization.v2018_07_01_preview.models.DenyAssignmentPaged[~azure.mgmt.authorization.v2018_07_01_preview.models.DenyAssignment]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_for_scope.metadata['url']
                path_format_arguments = {
                    'scope': self._serialize.url("scope", scope, 'str', skip_quote=True)
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
                if filter is not None:
                    query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def internal_paging(next_link=None):
            request = prepare_request(next_link)

            response = self._client.send(request, stream=False, **operation_config)

            if response.status_code not in [200]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            return response

        # Deserialize response
        header_dict = None
        if raw:
            header_dict = {}
        deserialized = models.DenyAssignmentPaged(internal_paging, self._deserialize.dependencies, header_dict)

        return deserialized
    list_for_scope.metadata = {'url': '/{scope}/providers/Microsoft.Authorization/denyAssignments'}
