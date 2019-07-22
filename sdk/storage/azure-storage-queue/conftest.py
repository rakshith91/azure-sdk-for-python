#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------

import sys


# Ignore async tests for Python < 3.5
collect_ignore = []
if sys.version_info < (3, 5):
    collect_ignore.append("tests/*_async.py")
