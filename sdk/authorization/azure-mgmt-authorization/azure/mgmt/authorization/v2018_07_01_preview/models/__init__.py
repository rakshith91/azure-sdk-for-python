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
    from ._models_py3 import DenyAssignment
    from ._models_py3 import DenyAssignmentFilter
    from ._models_py3 import DenyAssignmentPermission
    from ._models_py3 import Principal
except (SyntaxError, ImportError):
    from ._models import DenyAssignment
    from ._models import DenyAssignmentFilter
    from ._models import DenyAssignmentPermission
    from ._models import Principal
from ._paged_models import DenyAssignmentPaged

__all__ = [
    'DenyAssignment',
    'DenyAssignmentFilter',
    'DenyAssignmentPermission',
    'Principal',
    'DenyAssignmentPaged',
]
