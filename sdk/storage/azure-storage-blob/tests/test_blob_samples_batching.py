# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

import os
import sys
import pytest
try:
    import settings_real as settings
except ImportError:
    import blob_settings_fake as settings

from testcase import (
    StorageTestCase,
    TestMode,
    record
)

SOURCE_FILE = 'SampleSource.txt'
DEST_FILE = 'BlockDestination.txt'


class TestBlobBatchingSamples(StorageTestCase):

    connection_string = settings.CONNECTION_STRING

    def setUp(self):
        data = b"Lorem ipsum dolor sit amet, consectetur adipiscing elit"
        with open(SOURCE_FILE, 'wb') as stream:
            stream.write(data)

        super(TestBlobBatchingSamples, self).setUp()

    def tearDown(self):
        if os.path.isfile(SOURCE_FILE):
            try:
                os.remove(SOURCE_FILE)
            except:
                pass
        if os.path.isfile(DEST_FILE):
            try:
                os.remove(DEST_FILE)
            except:
                pass

        return super(TestBlobBatchingSamples, self).tearDown()

    #--Begin Blob Samples-----------------------------------------------------------------

    @pytest.mark.skipif(sys.version_info < (3, 0), reason="Batch not supported on Python 2.7")
    @record
    def test_delete_blobs_simple_500(self):

        # Instantiate the Blob Service Client
        from azure.storage.blob import BlobServiceClient
        blob_service_client = BlobServiceClient.from_connection_string(self.connection_string)

        # Create the container
        container = blob_service_client.get_container_client('batchsamplescontainer')
        try:
            container.create_container()
        except:
            pass
        data = b'hello world'

        # Create 500 blobs
        blob_list = []
        for i in range(100):
            try:
                name = 'blob' + str(i)
                blob_list.append(name)
                container.get_blob_client(name).upload_blob(data)
            except:
                pass

        failed = blob_list
        # Act
        retry_count = 5
        while retry_count:
            response = container.delete_blobs(*failed)
            failed = [i.request for i in response if i.status_code != 202]
            if not failed:
                break
            retry_count -= 1
        
        assert retry_count  == 5
        assert failed == []


