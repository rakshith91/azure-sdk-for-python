# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

import sys
import pytest
import uuid
import os

# Ignore async tests for Python < 3.5
collect_ignore_glob = []
if sys.version_info < (3, 5):
    collect_ignore_glob.append("tests/*_async.py")

TEST_QUEUE_PREFIX = 'pythonqueue'

def get_config():
    config = {}
    config['PROTOCOL'] = os.environ['PROTOCOL']
    config['STORAGE_ACCOUNT_NAME'] = os.environ['STORAGE_ACCOUNT_NAME']
    config['STORAGE_ACCOUNT_KEY'] = os.environ['STORAGE_ACCOUNT_KEY']
    return config

@pytest.fixture()
def queue_name():
    return TEST_QUEUE_PREFIX + str(uuid.uuid4())

@pytest.fixture()
def queue_service_client():  # pylint: disable=redefined-outer-name
    config = get_config()
    account_url = "{}://{}.queue.core.windows.net".format(
            config['PROTOCOL'],
            config['STORAGE_ACCOUNT_NAME']
        )
    credentials = {
            "account_name": config['STORAGE_ACCOUNT_NAME'],
            "account_key": config['STORAGE_ACCOUNT_KEY']
        }
    from azure.storage.queue.queue_service_client import QueueServiceClient
    client = QueueServiceClient(account_url, credentials)
    return client

@pytest.fixture()
def queue_client(queue_name, queue_service_client):
    client = queue_service_client.get_queue_client(queue_name)
    try:
        client.create_queue()
        yield client
    finally:
        client.delete_queue()
