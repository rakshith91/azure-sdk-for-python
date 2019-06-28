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

from msrest.serialization import Model


class ClassicAdministrator(Model):
    """Classic Administrators.

    :param id: The ID of the administrator.
    :type id: str
    :param name: The name of the administrator.
    :type name: str
    :param type: The type of the administrator.
    :type type: str
    :param email_address: The email address of the administrator.
    :type email_address: str
    :param role: The role of the administrator.
    :type role: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'email_address': {'key': 'properties.emailAddress', 'type': 'str'},
        'role': {'key': 'properties.role', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ClassicAdministrator, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
        self.type = kwargs.get('type', None)
        self.email_address = kwargs.get('email_address', None)
        self.role = kwargs.get('role', None)


class CloudError(Model):
    """CloudError.
    """

    _attribute_map = {
    }


class Permission(Model):
    """Role definition permissions.

    :param actions: Allowed actions.
    :type actions: list[str]
    :param not_actions: Denied actions.
    :type not_actions: list[str]
    """

    _attribute_map = {
        'actions': {'key': 'actions', 'type': '[str]'},
        'not_actions': {'key': 'notActions', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(Permission, self).__init__(**kwargs)
        self.actions = kwargs.get('actions', None)
        self.not_actions = kwargs.get('not_actions', None)


class ProviderOperation(Model):
    """Operation.

    :param name: The operation name.
    :type name: str
    :param display_name: The operation display name.
    :type display_name: str
    :param description: The operation description.
    :type description: str
    :param origin: The operation origin.
    :type origin: str
    :param properties: The operation properties.
    :type properties: object
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'origin': {'key': 'origin', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'object'},
    }

    def __init__(self, **kwargs):
        super(ProviderOperation, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.display_name = kwargs.get('display_name', None)
        self.description = kwargs.get('description', None)
        self.origin = kwargs.get('origin', None)
        self.properties = kwargs.get('properties', None)


class ProviderOperationsMetadata(Model):
    """Provider Operations metadata.

    :param id: The provider id.
    :type id: str
    :param name: The provider name.
    :type name: str
    :param type: The provider type.
    :type type: str
    :param display_name: The provider display name.
    :type display_name: str
    :param resource_types: The provider resource types
    :type resource_types:
     list[~azure.mgmt.authorization.v2015_07_01.models.ResourceType]
    :param operations: The provider operations.
    :type operations:
     list[~azure.mgmt.authorization.v2015_07_01.models.ProviderOperation]
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'resource_types': {'key': 'resourceTypes', 'type': '[ResourceType]'},
        'operations': {'key': 'operations', 'type': '[ProviderOperation]'},
    }

    def __init__(self, **kwargs):
        super(ProviderOperationsMetadata, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
        self.type = kwargs.get('type', None)
        self.display_name = kwargs.get('display_name', None)
        self.resource_types = kwargs.get('resource_types', None)
        self.operations = kwargs.get('operations', None)


class ResourceType(Model):
    """Resource Type.

    :param name: The resource type name.
    :type name: str
    :param display_name: The resource type display name.
    :type display_name: str
    :param operations: The resource type operations.
    :type operations:
     list[~azure.mgmt.authorization.v2015_07_01.models.ProviderOperation]
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'operations': {'key': 'operations', 'type': '[ProviderOperation]'},
    }

    def __init__(self, **kwargs):
        super(ResourceType, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.display_name = kwargs.get('display_name', None)
        self.operations = kwargs.get('operations', None)


class RoleAssignment(Model):
    """Role Assignments.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The role assignment ID.
    :vartype id: str
    :ivar name: The role assignment name.
    :vartype name: str
    :ivar type: The role assignment type.
    :vartype type: str
    :param properties: Role assignment properties.
    :type properties:
     ~azure.mgmt.authorization.v2015_07_01.models.RoleAssignmentPropertiesWithScope
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'RoleAssignmentPropertiesWithScope'},
    }

    def __init__(self, **kwargs):
        super(RoleAssignment, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.properties = kwargs.get('properties', None)


class RoleAssignmentCreateParameters(Model):
    """Role assignment create parameters.

    All required parameters must be populated in order to send to Azure.

    :param properties: Required. Role assignment properties.
    :type properties:
     ~azure.mgmt.authorization.v2015_07_01.models.RoleAssignmentProperties
    """

    _validation = {
        'properties': {'required': True},
    }

    _attribute_map = {
        'properties': {'key': 'properties', 'type': 'RoleAssignmentProperties'},
    }

    def __init__(self, **kwargs):
        super(RoleAssignmentCreateParameters, self).__init__(**kwargs)
        self.properties = kwargs.get('properties', None)


class RoleAssignmentFilter(Model):
    """Role Assignments filter.

    :param principal_id: Returns role assignment of the specific principal.
    :type principal_id: str
    """

    _attribute_map = {
        'principal_id': {'key': 'principalId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(RoleAssignmentFilter, self).__init__(**kwargs)
        self.principal_id = kwargs.get('principal_id', None)


class RoleAssignmentProperties(Model):
    """Role assignment properties.

    All required parameters must be populated in order to send to Azure.

    :param role_definition_id: Required. The role definition ID used in the
     role assignment.
    :type role_definition_id: str
    :param principal_id: Required. The principal ID assigned to the role. This
     maps to the ID inside the Active Directory. It can point to a user,
     service principal, or security group.
    :type principal_id: str
    """

    _validation = {
        'role_definition_id': {'required': True},
        'principal_id': {'required': True},
    }

    _attribute_map = {
        'role_definition_id': {'key': 'roleDefinitionId', 'type': 'str'},
        'principal_id': {'key': 'principalId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(RoleAssignmentProperties, self).__init__(**kwargs)
        self.role_definition_id = kwargs.get('role_definition_id', None)
        self.principal_id = kwargs.get('principal_id', None)


class RoleAssignmentPropertiesWithScope(Model):
    """Role assignment properties with scope.

    :param scope: The role assignment scope.
    :type scope: str
    :param role_definition_id: The role definition ID.
    :type role_definition_id: str
    :param principal_id: The principal ID.
    :type principal_id: str
    """

    _attribute_map = {
        'scope': {'key': 'scope', 'type': 'str'},
        'role_definition_id': {'key': 'roleDefinitionId', 'type': 'str'},
        'principal_id': {'key': 'principalId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(RoleAssignmentPropertiesWithScope, self).__init__(**kwargs)
        self.scope = kwargs.get('scope', None)
        self.role_definition_id = kwargs.get('role_definition_id', None)
        self.principal_id = kwargs.get('principal_id', None)


class RoleDefinition(Model):
    """Role definition.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The role definition ID.
    :vartype id: str
    :ivar name: The role definition name.
    :vartype name: str
    :ivar type: The role definition type.
    :vartype type: str
    :param role_name: The role name.
    :type role_name: str
    :param description: The role definition description.
    :type description: str
    :param role_type: The role type.
    :type role_type: str
    :param permissions: Role definition permissions.
    :type permissions:
     list[~azure.mgmt.authorization.v2015_07_01.models.Permission]
    :param assignable_scopes: Role definition assignable scopes.
    :type assignable_scopes: list[str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'role_name': {'key': 'properties.roleName', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'role_type': {'key': 'properties.type', 'type': 'str'},
        'permissions': {'key': 'properties.permissions', 'type': '[Permission]'},
        'assignable_scopes': {'key': 'properties.assignableScopes', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(RoleDefinition, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.role_name = kwargs.get('role_name', None)
        self.description = kwargs.get('description', None)
        self.role_type = kwargs.get('role_type', None)
        self.permissions = kwargs.get('permissions', None)
        self.assignable_scopes = kwargs.get('assignable_scopes', None)


class RoleDefinitionFilter(Model):
    """Role Definitions filter.

    :param role_name: Returns role definition with the specific name.
    :type role_name: str
    """

    _attribute_map = {
        'role_name': {'key': 'roleName', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(RoleDefinitionFilter, self).__init__(**kwargs)
        self.role_name = kwargs.get('role_name', None)
