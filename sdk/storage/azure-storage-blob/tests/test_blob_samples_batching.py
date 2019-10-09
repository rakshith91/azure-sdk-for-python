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

        # Create 500 blobs and put them in a list
        blob_list = []
        for i in range(500):
            try:
                name = 'blob' + str(i)
                blob_list.append(name)
                container.get_blob_client(name).upload_blob(data)
            except:
                pass

        # Number of retries. This way we ensure we don't keep retrying deleting something that is expected to return 404.
        # for example, deleteing snapshot "only" when there is no snapshot.
        retry_count = 5

        # Max allowed in a single batch
        max_allowed = 256

        # start the loop
        while retry_count:

            # split into two lists: first 256, remaining items (if length is less than 256, second
            # slice will simply be empty)
            batch_list, remaining_list =  blob_list[:max_allowed],  blob_list[max_allowed:]

            # delete_blobs; upto 256
            response = container.delete_blobs(*batch_list)

            # list of failed blob names
            failed = [blob for blob, res in zip(batch_list, response) if res.status_code != 202]

            # update the blob_list
            blob_list = failed + remaining_blob_list
            if not blob_list:
                break
            retry_count -= 1

        assert blob_list == []
