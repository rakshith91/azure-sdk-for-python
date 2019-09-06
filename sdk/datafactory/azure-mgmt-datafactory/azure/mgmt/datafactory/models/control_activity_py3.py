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

from .activity_py3 import Activity


class ControlActivity(Activity):
    """Base class for all control activities like IfCondition, ForEach , Until.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: WebHookActivity, AppendVariableActivity,
    SetVariableActivity, FilterActivity, ValidationActivity, UntilActivity,
    WaitActivity, ForEachActivity, IfConditionActivity, ExecutePipelineActivity

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param name: Required. Activity name.
    :type name: str
    :param description: Activity description.
    :type description: str
    :param depends_on: Activity depends on condition.
    :type depends_on: list[~azure.mgmt.datafactory.models.ActivityDependency]
    :param user_properties: Activity user properties.
    :type user_properties: list[~azure.mgmt.datafactory.models.UserProperty]
    :param type: Required. Constant filled by server.
    :type type: str
    """

    _validation = {
        'name': {'required': True},
        'type': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'depends_on': {'key': 'dependsOn', 'type': '[ActivityDependency]'},
        'user_properties': {'key': 'userProperties', 'type': '[UserProperty]'},
        'type': {'key': 'type', 'type': 'str'},
    }

    _subtype_map = {
        'type': {'WebHook': 'WebHookActivity', 'AppendVariable': 'AppendVariableActivity', 'SetVariable': 'SetVariableActivity', 'Filter': 'FilterActivity', 'Validation': 'ValidationActivity', 'Until': 'UntilActivity', 'Wait': 'WaitActivity', 'ForEach': 'ForEachActivity', 'IfCondition': 'IfConditionActivity', 'ExecutePipeline': 'ExecutePipelineActivity'}
    }

    def __init__(self, *, name: str, additional_properties=None, description: str=None, depends_on=None, user_properties=None, **kwargs) -> None:
        super(ControlActivity, self).__init__(additional_properties=additional_properties, name=name, description=description, depends_on=depends_on, user_properties=user_properties, **kwargs)
        self.type = 'Container'
