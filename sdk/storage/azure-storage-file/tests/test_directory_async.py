# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import unittest
import asyncio

from azure.core.exceptions import ResourceNotFoundError, ResourceExistsError
from azure.core.pipeline.transport import AioHttpTransport
from devtools_testutils import ResourceGroupPreparer, StorageAccountPreparer, FakeStorageAccount
from multidict import CIMultiDict, CIMultiDictProxy
from azure.storage.file.aio import (
    FileServiceClient,
    StorageErrorCode,
)
from asyncfiletestcase import (
    AsyncFileTestCase
)


FAKE_STORAGE = FakeStorageAccount(
    name='pyacrstorage',
    id='')

# ------------------------------------------------------------------------------

class AiohttpTestTransport(AioHttpTransport):
    """Workaround to vcrpy bug: https://github.com/kevin1024/vcrpy/pull/461
    """
    async def send(self, request, **config):
        response = await super(AiohttpTestTransport, self).send(request, **config)
        if not isinstance(response.headers, CIMultiDictProxy):
            response.headers = CIMultiDictProxy(CIMultiDict(response.internal_response.headers))
            response.content_type = response.headers.get("content-type")
        return response


class StorageDirectoryTest(AsyncFileTestCase):
    def setUp(self):
        super(StorageDirectoryTest, self).setUp()
        self.share_name = self.get_resource_name('utshare')

    # --Helpers-----------------------------------------------------------------
    async def _setup(self, fsc):
        if self.is_live:
            try:
                await fsc.create_share(self.share_name)
            except:
                pass

    # --Test cases for directories ----------------------------------------------
    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage', playback_fake_resource=FAKE_STORAGE)
    @AsyncFileTestCase.await_prepared_test
    async def test_create_directories_async(self, resource_group, location, storage_account, storage_account_key):
        # Arrange
        fsc = FileServiceClient(self._account_url(storage_account.name), credential=storage_account_key, transport=AiohttpTestTransport())
        await self._setup(fsc)
        share_client = fsc.get_share_client(self.share_name)

        # Act
        created = await share_client.create_directory('dir1')

        # Assert
        self.assertTrue(created)

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage', playback_fake_resource=FAKE_STORAGE)
    @AsyncFileTestCase.await_prepared_test
    async def test_create_directories_with_metadata_async(self, resource_group, location, storage_account, storage_account_key):
        # Arrange
        fsc = FileServiceClient(self._account_url(storage_account.name), credential=storage_account_key, transport=AiohttpTestTransport())
        await self._setup(fsc)
        share_client = fsc.get_share_client(self.share_name)
        metadata = {'hello': 'world', 'number': '42'}

        # Act
        directory = await share_client.create_directory('dir1', metadata=metadata)

        # Assert
        props = await directory.get_directory_properties()
        self.assertDictEqual(props.metadata, metadata)

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage', playback_fake_resource=FAKE_STORAGE)
    @AsyncFileTestCase.await_prepared_test
    async def test_create_directories_fail_on_exist_async(self, resource_group, location, storage_account, storage_account_key):
        # Arrange
        fsc = FileServiceClient(self._account_url(storage_account.name), credential=storage_account_key, transport=AiohttpTestTransport())
        await self._setup(fsc)
        share_client = fsc.get_share_client(self.share_name)

        # Act
        created = await share_client.create_directory('dir1')
        with self.assertRaises(ResourceExistsError):
            await share_client.create_directory('dir1')

        # Assert
        self.assertTrue(created)

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage', playback_fake_resource=FAKE_STORAGE)
    @AsyncFileTestCase.await_prepared_test
    async def test_create_subdirectories_async(self, resource_group, location, storage_account, storage_account_key):
        # Arrange
        fsc = FileServiceClient(self._account_url(storage_account.name), credential=storage_account_key, transport=AiohttpTestTransport())
        await self._setup(fsc)
        share_client = fsc.get_share_client(self.share_name)
        directory = await share_client.create_directory('dir1')

        # Act
        created = await directory.create_subdirectory('dir2')

        # Assert
        self.assertTrue(created)
        self.assertEqual(created.directory_path, 'dir1/dir2')


    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage', playback_fake_resource=FAKE_STORAGE)
    @AsyncFileTestCase.await_prepared_test
    async def test_create_subdirectories_with_metadata_async(self, resource_group, location, storage_account, storage_account_key):
        # Arrange
        fsc = FileServiceClient(self._account_url(storage_account.name), credential=storage_account_key, transport=AiohttpTestTransport())
        await self._setup(fsc)
        share_client = fsc.get_share_client(self.share_name)
        directory = await share_client.create_directory('dir1')
        metadata = {'hello': 'world', 'number': '42'}

        # Act
        created = await directory.create_subdirectory('dir2', metadata=metadata)

        # Assert
        self.assertTrue(created)
        self.assertEqual(created.directory_path, 'dir1/dir2')
        properties = await created.get_directory_properties()
        self.assertEqual(properties.metadata, metadata)

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage', playback_fake_resource=FAKE_STORAGE)
    @AsyncFileTestCase.await_prepared_test
    async def test_create_file_in_directory_async(self, resource_group, location, storage_account, storage_account_key):
        # Arrange
        fsc = FileServiceClient(self._account_url(storage_account.name), credential=storage_account_key, transport=AiohttpTestTransport())
        await self._setup(fsc)
        file_data = b'12345678' * 1024
        file_name = self.get_resource_name('file')
        share_client = fsc.get_share_client(self.share_name)
        directory = await share_client.create_directory('dir1')

        # Act
        new_file = await directory.upload_file(file_name, file_data)

        # Assert
        file_content = await new_file.download_file()
        file_content = await file_content.content_as_bytes()
        self.assertEqual(file_content, file_data)

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage', playback_fake_resource=FAKE_STORAGE)
    @AsyncFileTestCase.await_prepared_test
    async def test_delete_file_in_directory_async(self, resource_group, location, storage_account, storage_account_key):
        # Arrange
        fsc = FileServiceClient(self._account_url(storage_account.name), credential=storage_account_key, transport=AiohttpTestTransport())
        await self._setup(fsc)
        file_name = self.get_resource_name('file')
        share_client = fsc.get_share_client(self.share_name)
        directory = await share_client.create_directory('dir1')
        new_file = await directory.upload_file(file_name, "hello world")

        # Act
        deleted = await directory.delete_file(file_name)

        # Assert
        self.assertIsNone(deleted)
        with self.assertRaises(ResourceNotFoundError):
            await new_file.get_file_properties()

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage', playback_fake_resource=FAKE_STORAGE)
    @AsyncFileTestCase.await_prepared_test
    async def test_delete_subdirectories_async(self, resource_group, location, storage_account, storage_account_key):
        # Arrange
        fsc = FileServiceClient(self._account_url(storage_account.name), credential=storage_account_key, transport=AiohttpTestTransport())
        await self._setup(fsc)
        share_client = fsc.get_share_client(self.share_name)
        directory = await share_client.create_directory('dir1')
        await directory.create_subdirectory('dir2')

        # Act
        deleted = await directory.delete_subdirectory('dir2')

        # Assert
        self.assertIsNone(deleted)
        subdir = directory.get_subdirectory_client('dir2')
        with self.assertRaises(ResourceNotFoundError):
            await subdir.get_directory_properties()

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage', playback_fake_resource=FAKE_STORAGE)
    @AsyncFileTestCase.await_prepared_test
    async def test_get_directory_properties_async(self, resource_group, location, storage_account, storage_account_key):
        # Arrange
        fsc = FileServiceClient(self._account_url(storage_account.name), credential=storage_account_key, transport=AiohttpTestTransport())
        await self._setup(fsc)
        share_client = fsc.get_share_client(self.share_name)
        directory = await share_client.create_directory('dir1')

        # Act
        props = await directory.get_directory_properties()

        # Assert
        self.assertIsNotNone(props)
        self.assertIsNotNone(props.etag)
        self.assertIsNotNone(props.last_modified)

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage', playback_fake_resource=FAKE_STORAGE)
    @AsyncFileTestCase.await_prepared_test
    async def test_get_directory_properties_with_snapshot_async(self, resource_group, location, storage_account, storage_account_key):
        # Arrange
        fsc = FileServiceClient(self._account_url(storage_account.name), credential=storage_account_key, transport=AiohttpTestTransport())
        await self._setup(fsc)
        share_client = fsc.get_share_client(self.share_name)
        metadata = {"test1": "foo", "test2": "bar"}
        directory = await share_client.create_directory('dir1', metadata=metadata)
        snapshot1 = await share_client.create_snapshot()
        metadata2 = {"test100": "foo100", "test200": "bar200"}
        await directory.set_directory_metadata(metadata2)

        # Act
        share_client = fsc.get_share_client(self.share_name, snapshot=snapshot1)
        snap_dir = share_client.get_directory_client('dir1')
        props = await snap_dir.get_directory_properties()

        # Assert
        self.assertIsNotNone(props)
        self.assertIsNotNone(props.etag)
        self.assertIsNotNone(props.last_modified)
        self.assertDictEqual(metadata, props.metadata)

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage', playback_fake_resource=FAKE_STORAGE)
    @AsyncFileTestCase.await_prepared_test
    async def test_get_directory_metadata_with_snapshot_async(self, resource_group, location, storage_account, storage_account_key):
        # Arrange
        fsc = FileServiceClient(self._account_url(storage_account.name), credential=storage_account_key, transport=AiohttpTestTransport())
        await self._setup(fsc)
        share_client = fsc.get_share_client(self.share_name)
        metadata = {"test1": "foo", "test2": "bar"}
        directory = await share_client.create_directory('dir1', metadata=metadata)
        snapshot1 = await share_client.create_snapshot()
        metadata2 = {"test100": "foo100", "test200": "bar200"}
        await directory.set_directory_metadata(metadata2)

        # Act
        share_client = fsc.get_share_client(self.share_name, snapshot=snapshot1)
        snap_dir = share_client.get_directory_client('dir1')
        snapshot_props = await snap_dir.get_directory_properties()

        # Assert
        self.assertIsNotNone(snapshot_props.metadata)
        self.assertDictEqual(metadata, snapshot_props.metadata)

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage', playback_fake_resource=FAKE_STORAGE)
    @AsyncFileTestCase.await_prepared_test
    async def test_get_dir_proos_with_non_existing_dir_async(self, resource_group, location, storage_account, storage_account_key):
        # Arrange
        fsc = FileServiceClient(self._account_url(storage_account.name), credential=storage_account_key, transport=AiohttpTestTransport())
        await self._setup(fsc)
        share_client = fsc.get_share_client(self.share_name)
        directory = share_client.get_directory_client('dir1')

        # Act
        with self.assertRaises(ResourceNotFoundError):
            await directory.get_directory_properties()

            # Assert

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage', playback_fake_resource=FAKE_STORAGE)
    @AsyncFileTestCase.await_prepared_test
    async def test_directory_exists_async(self, resource_group, location, storage_account, storage_account_key):
        # Arrange
        fsc = FileServiceClient(self._account_url(storage_account.name), credential=storage_account_key, transport=AiohttpTestTransport())
        await self._setup(fsc)
        share_client = fsc.get_share_client(self.share_name)
        directory = await share_client.create_directory('dir1')

        # Act
        exists = await directory.get_directory_properties()

        # Assert
        self.assertTrue(exists)

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage', playback_fake_resource=FAKE_STORAGE)
    @AsyncFileTestCase.await_prepared_test
    async def test_directory_not_exists_async(self, resource_group, location, storage_account, storage_account_key):
        # Arrange
        fsc = FileServiceClient(self._account_url(storage_account.name), credential=storage_account_key, transport=AiohttpTestTransport())
        await self._setup(fsc)
        share_client = fsc.get_share_client(self.share_name)
        directory = share_client.get_directory_client('dir1')

        # Act
        with self.assertRaises(ResourceNotFoundError):
            await directory.get_directory_properties()

        # Assert

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage', playback_fake_resource=FAKE_STORAGE)
    @AsyncFileTestCase.await_prepared_test
    async def test_directory_parent_not_exists_async(self, resource_group, location, storage_account, storage_account_key):
        # Arrange
        fsc = FileServiceClient(self._account_url(storage_account.name), credential=storage_account_key, transport=AiohttpTestTransport())
        await self._setup(fsc)
        share_client = fsc.get_share_client(self.share_name)
        directory = share_client.get_directory_client('missing1/missing2')

        # Act
        with self.assertRaises(ResourceNotFoundError) as e:
            await directory.get_directory_properties()

        # Assert
        self.assertEqual(e.exception.error_code, StorageErrorCode.parent_not_found)

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage', playback_fake_resource=FAKE_STORAGE)
    @AsyncFileTestCase.await_prepared_test
    async def test_directory_exists_with_snapshot_async(self, resource_group, location, storage_account, storage_account_key):
        # Arrange
        fsc = FileServiceClient(self._account_url(storage_account.name), credential=storage_account_key, transport=AiohttpTestTransport())
        await self._setup(fsc)
        share_client = fsc.get_share_client(self.share_name)
        directory = await share_client.create_directory('dir1')
        snapshot = await share_client.create_snapshot()
        await directory.delete_directory()

        # Act
        share_client = fsc.get_share_client(self.share_name, snapshot=snapshot)
        snap_dir = share_client.get_directory_client('dir1')
        exists = await snap_dir.get_directory_properties()

        # Assert
        self.assertTrue(exists)

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage', playback_fake_resource=FAKE_STORAGE)
    @AsyncFileTestCase.await_prepared_test
    async def test_directory_not_exists_with_snapshot_async(self, resource_group, location, storage_account, storage_account_key):
        # Arrange
        fsc = FileServiceClient(self._account_url(storage_account.name), credential=storage_account_key, transport=AiohttpTestTransport())
        await self._setup(fsc)
        share_client = fsc.get_share_client(self.share_name)
        snapshot = await share_client.create_snapshot()
        directory = await share_client.create_directory('dir1')

        # Act
        share_client = fsc.get_share_client(self.share_name, snapshot=snapshot)
        snap_dir = share_client.get_directory_client('dir1')

        with self.assertRaises(ResourceNotFoundError):
            await snap_dir.get_directory_properties()

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage', playback_fake_resource=FAKE_STORAGE)
    @AsyncFileTestCase.await_prepared_test
    async def test_get_set_directory_metadata_async(self, resource_group, location, storage_account, storage_account_key):
        # Arrange
        fsc = FileServiceClient(self._account_url(storage_account.name), credential=storage_account_key, transport=AiohttpTestTransport())
        await self._setup(fsc)
        share_client = fsc.get_share_client(self.share_name)
        directory = await share_client.create_directory('dir1')
        metadata = {'hello': 'world', 'number': '43'}

        # Act
        await directory.set_directory_metadata(metadata)
        props = await directory.get_directory_properties()

        # Assert
        self.assertDictEqual(props.metadata, metadata)

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage', playback_fake_resource=FAKE_STORAGE)
    @AsyncFileTestCase.await_prepared_test
    async def test_list_subdirectories_and_files_async(self):
        # Arrange
        fsc = FileServiceClient(self._account_url(storage_account.name), credential=storage_account_key, transport=AiohttpTestTransport())
        await self._setup(fsc)
        share_client = fsc.get_share_client(self.share_name)
        directory = await share_client.create_directory('dir1')
        await asyncio.gather(
            directory.create_subdirectory("subdir1"),
            directory.create_subdirectory("subdir2"),
            directory.create_subdirectory("subdir3"),
            directory.upload_file("file1", "data1"),
            directory.upload_file("file2", "data2"),
            directory.upload_file("file3", "data3"))

        # Act
        list_dir = []
        async for d in directory.list_directories_and_files():
            list_dir.append(d)

        # Assert
        expected = [
            {'name': 'subdir1', 'is_directory': True},
            {'name': 'subdir2', 'is_directory': True},
            {'name': 'subdir3', 'is_directory': True},
            {'name': 'file1', 'is_directory': False, 'size': 5},
            {'name': 'file2', 'is_directory': False, 'size': 5},
            {'name': 'file3', 'is_directory': False, 'size': 5},
        ]
        self.assertEqual(len(list_dir), 6)
        self.assertEqual(list_dir, expected)

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage', playback_fake_resource=FAKE_STORAGE)
    @AsyncFileTestCase.await_prepared_test
    async def test_list_subdirectories_and_files_with_prefix_async(self, resource_group, location, storage_account, storage_account_key):
        # Arrange
        fsc = FileServiceClient(self._account_url(storage_account.name), credential=storage_account_key, transport=AiohttpTestTransport())
        await self._setup(fsc)
        share_client = fsc.get_share_client(self.share_name)
        directory = await share_client.create_directory('dir1')
        await asyncio.gather(
            directory.create_subdirectory("subdir1"),
            directory.create_subdirectory("subdir2"),
            directory.create_subdirectory("subdir3"),
            directory.upload_file("file1", "data1"),
            directory.upload_file("file2", "data2"),
            directory.upload_file("file3", "data3"))

        # Act
        list_dir = []
        async for d in directory.list_directories_and_files(name_starts_with="sub"):
            list_dir.append(d)

        # Assert
        expected = [
            {'name': 'subdir1', 'is_directory': True},
            {'name': 'subdir2', 'is_directory': True},
            {'name': 'subdir3', 'is_directory': True},
        ]
        self.assertEqual(len(list_dir), 3)
        self.assertEqual(list_dir, expected)

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage', playback_fake_resource=FAKE_STORAGE)
    @AsyncFileTestCase.await_prepared_test
    async def test_list_subdirectories_and_files_with_snapshot_async(self, resource_group, location, storage_account, storage_account_key):
        # Arrange
        fsc = FileServiceClient(self._account_url(storage_account.name), credential=storage_account_key, transport=AiohttpTestTransport())
        await self._setup(fsc)
        share_client = fsc.get_share_client(self.share_name)
        directory = await share_client.create_directory('dir1')
        await asyncio.gather(
            directory.create_subdirectory("subdir1"),
            directory.create_subdirectory("subdir2"),
            directory.upload_file("file1", "data1"))
        
        snapshot = await share_client.create_snapshot()
        await asyncio.gather(
            directory.create_subdirectory("subdir3"),
            directory.upload_file("file2", "data2"),
            directory.upload_file("file3", "data3"))

        share_client = fsc.get_share_client(self.share_name, snapshot=snapshot)
        snapshot_dir = share_client.get_directory_client('dir1')

        # Act
        list_dir = []
        async for d in snapshot_dir.list_directories_and_files():
            list_dir.append(d)

        # Assert
        expected = [
            {'name': 'subdir1', 'is_directory': True},
            {'name': 'subdir2', 'is_directory': True},
            {'name': 'file1', 'is_directory': False, 'size': 5},
        ]
        self.assertEqual(len(list_dir), 3)
        self.assertEqual(list_dir, expected)


    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage', playback_fake_resource=FAKE_STORAGE)
    @AsyncFileTestCase.await_prepared_test
    async def test_list_nested_subdirectories_and_files_async(self, resource_group, location, storage_account, storage_account_key):
        # Arrange
        fsc = FileServiceClient(self._account_url(storage_account.name), credential=storage_account_key, transport=AiohttpTestTransport())
        await self._setup(fsc)
        share_client = fsc.get_share_client(self.share_name)
        directory = await share_client.create_directory('dir1')
        subdir = await directory.create_subdirectory("subdir1")
        await subdir.create_subdirectory("subdir2")
        await subdir.create_subdirectory("subdir3")
        await asyncio.gather(
            directory.upload_file("file1", "data1"),
            subdir.upload_file("file2", "data2"),
            subdir.upload_file("file3", "data3"))

        # Act
        list_dir = []
        async for d in directory.list_directories_and_files():
            list_dir.append(d)

        # Assert
        expected = [
            {'name': 'subdir1', 'is_directory': True},
            {'name': 'file1', 'is_directory': False, 'size': 5},
        ]
        self.assertEqual(len(list_dir), 2)
        self.assertEqual(list_dir, expected)


    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage', playback_fake_resource=FAKE_STORAGE)
    @AsyncFileTestCase.await_prepared_test
    async def test_delete_directory_with_existing_share_async(self, resource_group, location, storage_account, storage_account_key):
        # Arrange
        fsc = FileServiceClient(self._account_url(storage_account.name), credential=storage_account_key, transport=AiohttpTestTransport())
        await self._setup(fsc)
        share_client = fsc.get_share_client(self.share_name)
        directory = await share_client.create_directory('dir1')

        # Act
        deleted = await directory.delete_directory()

        # Assert
        self.assertIsNone(deleted)
        with self.assertRaises(ResourceNotFoundError):
            await directory.get_directory_properties()


    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage', playback_fake_resource=FAKE_STORAGE)
    @AsyncFileTestCase.await_prepared_test
    async def test_delete_directory_with_non_existing_directory_async(self, resource_group, location, storage_account, storage_account_key):
        # Arrange
        fsc = FileServiceClient(self._account_url(storage_account.name), credential=storage_account_key, transport=AiohttpTestTransport())
        await self._setup(fsc)
        share_client = fsc.get_share_client(self.share_name)
        directory = share_client.get_directory_client('dir1')

        # Act
        with self.assertRaises(ResourceNotFoundError):
            await directory.delete_directory()

        # Assert


    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage', playback_fake_resource=FAKE_STORAGE)
    @AsyncFileTestCase.await_prepared_test
    async def test_get_directory_properties_server_encryption_async(self, resource_group, location, storage_account, storage_account_key):
        # Arrange
        fsc = FileServiceClient(self._account_url(storage_account.name), credential=storage_account_key, transport=AiohttpTestTransport())
        await self._setup(fsc)
        share_client = fsc.get_share_client(self.share_name)
        directory = await share_client.create_directory('dir1')

        # Act
        props = await directory.get_directory_properties()

        # Assert
        self.assertIsNotNone(props)
        self.assertIsNotNone(props.etag)
        self.assertIsNotNone(props.last_modified)

        if self.is_file_encryption_enabled():
            self.assertTrue(props.server_encrypted)
        else:
            self.assertFalse(props.server_encrypted)

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
