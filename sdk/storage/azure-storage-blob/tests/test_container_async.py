# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
import unittest
import asyncio
from dateutil.tz import tzutc

import requests
from datetime import datetime, timedelta

from azure.core.exceptions import HttpResponseError, ResourceNotFoundError, ResourceExistsError
from azure.core.pipeline.transport import AioHttpTransport
from multidict import CIMultiDict, CIMultiDictProxy
from devtools_testutils import ResourceGroupPreparer, StorageAccountPreparer
from azure.storage.blob.aio import (
    BlobServiceClient,
    ContainerClient,
    BlobClient,
    PublicAccess,
    LeaseClient,
    AccessPolicy,
    StorageErrorCode,
    BlobBlock,
    BlobType,
    ContentSettings,
    BlobProperties,
    ContainerPermissions
)

from testcase import LogCaptured
from asyncblobtestcase import (
    AsyncBlobTestCase,
)

#------------------------------------------------------------------------------
TEST_CONTAINER_PREFIX = 'container'
#------------------------------------------------------------------------------

class AiohttpTestTransport(AioHttpTransport):
    """Workaround to vcrpy bug: https://github.com/kevin1024/vcrpy/pull/461
    """
    async def send(self, request, **config):
        response = await super(AiohttpTestTransport, self).send(request, **config)
        if not isinstance(response.headers, CIMultiDictProxy):
            response.headers = CIMultiDictProxy(CIMultiDict(response.internal_response.headers))
            response.content_type = response.headers.get("content-type")
        return response


class StorageContainerTestAsync(StorageTestCase):

    #--Helpers-----------------------------------------------------------------
    def _get_container_reference(self, prefix=TEST_CONTAINER_PREFIX):
        container_name = self.get_resource_name(prefix)
        return container_name

    async def _create_container(self, bsc, prefix=TEST_CONTAINER_PREFIX):
        container_name = self._get_container_reference(prefix)
        container = bsc.get_container_client(container_name)
        try:
            await container.create_container()
        except ResourceExistsError:
            pass
        return container

    #--Test cases for containers -----------------------------------------
    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    @AsyncBlobTestCase.await_prepared_test
    async def test_create_container(self, resource_group, location, storage_account, storage_account_key):
        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key, transport=AiohttpTestTransport())
        container_name = self._get_container_reference()

        # Act
        container = bsc.get_container_client(container_name)
        created = await container.create_container()

        # Assert
        self.assertTrue(created)

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    @AsyncBlobTestCase.await_prepared_test
    async def test_create_container_with_already_existing_container_fail_on_exist(self, resource_group, location, storage_account, storage_account_key):
        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key, transport=AiohttpTestTransport())
        container_name = self._get_container_reference()

        # Act
        container = bsc.get_container_client(container_name)
        created = await container.create_container()
        with self.assertRaises(HttpResponseError):
            await container.create_container()

        # Assert
        self.assertTrue(created)

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    @AsyncBlobTestCase.await_prepared_test
    async def test_create_container_with_public_access_container(self, resource_group, location, storage_account, storage_account_key):
        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key, transport=AiohttpTestTransport())
        container_name = self._get_container_reference()

        # Act
        container = bsc.get_container_client(container_name)
        created = await container.create_container(public_access='container')

        # Assert
        self.assertTrue(created)

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    @AsyncBlobTestCase.await_prepared_test
    async def test_create_container_with_public_access_blob(self, resource_group, location, storage_account, storage_account_key):
        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key, transport=AiohttpTestTransport())
        container_name = self._get_container_reference()

        # Act
        container = bsc.get_container_client(container_name)
        created = await container.create_container(public_access='blob')

        blob = container.get_blob_client("blob1")
        await blob.upload_blob(u'xyz')

        anonymous_service = BlobClient(
            self._get_account_url(),
            container=container_name,
            blob="blob1")

        # Assert
        self.assertTrue(created)
        await anonymous_service.download_blob()

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    @AsyncBlobTestCase.await_prepared_test
    async def test_create_container_with_metadata(self, resource_group, location, storage_account, storage_account_key):
        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key, transport=AiohttpTestTransport())
        container_name = self._get_container_reference()
        metadata = {'hello': 'world', 'number': '42'}

        # Act
        container = bsc.get_container_client(container_name)
        created = await container.create_container(metadata)

        # Assert
        self.assertTrue(created)
        md_cr = await container.get_container_properties()
        md = md_cr.metadata
        self.assertDictEqual(md, metadata)

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    @AsyncBlobTestCase.await_prepared_test
    async def test_container_exists_with_lease(self, resource_group, location, storage_account, storage_account_key):
        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key, transport=AiohttpTestTransport())
        container = await self._create_container(bsc)
        await container.acquire_lease()

        # Act
        exists = await container.get_container_properties()

        # Assert
        self.assertTrue(exists)

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    @AsyncBlobTestCase.await_prepared_test
    async def test_unicode_create_container_unicode_name(self, resource_group, location, storage_account, storage_account_key):
        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key, transport=AiohttpTestTransport())
        container_name = u'啊齄丂狛狜'

        container = bsc.get_container_client(container_name)
        # Act
        with self.assertRaises(HttpResponseError):
            # not supported - container name must be alphanumeric, lowercase
            await container.create_container()

        # Assert

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    @AsyncBlobTestCase.await_prepared_test
    async def test_list_containers(self, resource_group, location, storage_account, storage_account_key):
        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key, transport=AiohttpTestTransport())
        container = await self._create_container(bsc)

        # Act
        containers = []
        async for c in bsc.list_containers():
            containers.append(c)


        # Assert
        self.assertIsNotNone(containers)
        self.assertGreaterEqual(len(containers), 1)
        self.assertIsNotNone(containers[0])
        self.assert_named_item_in_container(containers, container.container_name)
        self.assertIsNotNone(containers[0].has_immutability_policy)
        self.assertIsNotNone(containers[0].has_legal_hold)

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    @AsyncBlobTestCase.await_prepared_test
    async def test_list_containers_with_prefix(self, resource_group, location, storage_account, storage_account_key):
        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key, transport=AiohttpTestTransport())
        container = await self._create_container(bsc)

        # Act
        containers = []
        async for c in bsc.list_containers(name_starts_with=container.container_name):
            containers.append(c)

        # Assert
        self.assertIsNotNone(containers)
        self.assertEqual(len(containers), 1)
        self.assertIsNotNone(containers[0])
        self.assertEqual(containers[0].name, container.container_name)
        self.assertIsNone(containers[0].metadata)

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    @AsyncBlobTestCase.await_prepared_test
    async def test_list_containers_with_include_metadata(self, resource_group, location, storage_account, storage_account_key):
        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key, transport=AiohttpTestTransport())
        container = await self._create_container(bsc)
        metadata = {'hello': 'world', 'number': '42'}
        resp = await container.set_container_metadata(metadata)

        # Act
        containers = []
        async for c in bsc.list_containers(
            name_starts_with=container.container_name,
            include_metadata=True):
            containers.append(c)

        # Assert
        self.assertIsNotNone(containers)
        self.assertGreaterEqual(len(containers), 1)
        self.assertIsNotNone(containers[0])
        self.assert_named_item_in_container(containers, container.container_name)
        self.assertDictEqual(containers[0].metadata, metadata)

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    @AsyncBlobTestCase.await_prepared_test
    async def test_list_containers_with_public_access(self, resource_group, location, storage_account, storage_account_key):
        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key, transport=AiohttpTestTransport())
        container = await self._create_container(bsc)
        resp = await container.set_container_access_policy(public_access=PublicAccess.Blob)

        # Act
        containers = []
        async for c in bsc.list_containers(name_starts_with=container.container_name):
            containers.append(c)

        # Assert
        self.assertIsNotNone(containers)
        self.assertGreaterEqual(len(containers), 1)
        self.assertIsNotNone(containers[0])
        self.assert_named_item_in_container(containers, container.container_name)
        self.assertEqual(containers[0].public_access, PublicAccess.Blob)

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    @AsyncBlobTestCase.await_prepared_test
    async def test_list_containers_with_num_results_and_marker(self, resource_group, location, storage_account, storage_account_key):
        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key, transport=AiohttpTestTransport())
        prefix = 'listcontainer'
        container_names = []
        for i in range(0, 4):
            cr = await self._create_container(bsc, prefix + str(i))
            container_names.append(cr.container_name)

        container_names.sort()

        # Act
        generator1 = bsc.list_containers(name_starts_with=prefix, results_per_page=2).by_page()
        containers1 = []
        async for c in await generator1.__anext__():
            containers1.append(c)

        generator2 = bsc.list_containers(
            name_starts_with=prefix, results_per_page=2).by_page(generator1.continuation_token)
        containers2 = []
        async for c in await generator2.__anext__():
            containers2.append(c)

        # Assert
        self.assertIsNotNone(containers1)
        self.assertEqual(len(containers1), 2)
        self.assert_named_item_in_container(containers1, container_names[0])
        self.assert_named_item_in_container(containers1, container_names[1])
        self.assertIsNotNone(containers2)
        self.assertEqual(len(containers2), 2)
        self.assert_named_item_in_container(containers2, container_names[2])
        self.assert_named_item_in_container(containers2, container_names[3])

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    @AsyncBlobTestCase.await_prepared_test
    async def test_set_container_metadata(self, resource_group, location, storage_account, storage_account_key):
        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key, transport=AiohttpTestTransport())
        metadata = {'hello': 'world', 'number': '43'}
        container = await self._create_container(bsc)

        # Act
        await container.set_container_metadata(metadata)
        md = await container.get_container_properties()
        metadata_from_response = md.metadata
        # Assert
        self.assertDictEqual(metadata_from_response, metadata)

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    @AsyncBlobTestCase.await_prepared_test
    async def test_set_container_metadata_with_lease_id(self, resource_group, location, storage_account, storage_account_key):
        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key, transport=AiohttpTestTransport())
        metadata = {'hello': 'world', 'number': '43'}
        container = await self._create_container(bsc)
        lease_id = await container.acquire_lease()

        # Act
        await container.set_container_metadata(metadata, lease_id)

        # Assert
        md = await container.get_container_properties()
        md = md.metadata
        self.assertDictEqual(md, metadata)

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    @AsyncBlobTestCase.await_prepared_test
    async def test_set_container_metadata_with_non_existing_container(self, resource_group, location, storage_account, storage_account_key):
        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key, transport=AiohttpTestTransport())
        container_name = self._get_container_reference()
        container = bsc.get_container_client(container_name)

        # Act
        with self.assertRaises(ResourceNotFoundError):
            await container.set_container_metadata({'hello': 'world', 'number': '43'})

        # Assert

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    @AsyncBlobTestCase.await_prepared_test
    async def test_get_container_metadata(self, resource_group, location, storage_account, storage_account_key):
        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key, transport=AiohttpTestTransport())
        metadata = {'hello': 'world', 'number': '42'}
        container = await self._create_container(bsc)
        await container.set_container_metadata(metadata)

        # Act
        md_cr = await container.get_container_properties()
        md = md_cr.metadata

        # Assert
        self.assertDictEqual(md, metadata)

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    @AsyncBlobTestCase.await_prepared_test
    async def test_get_container_metadata_with_lease_id(self, resource_group, location, storage_account, storage_account_key):
        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key, transport=AiohttpTestTransport())
        metadata = {'hello': 'world', 'number': '42'}
        container = await self._create_container(bsc)
        await container.set_container_metadata(metadata)
        lease_id = await container.acquire_lease()

        # Act
        md = await container.get_container_properties(lease_id)
        md = md.metadata

        # Assert
        self.assertDictEqual(md, metadata)

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    @AsyncBlobTestCase.await_prepared_test
    async def test_get_container_properties(self, resource_group, location, storage_account, storage_account_key):
        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key, transport=AiohttpTestTransport())
        metadata = {'hello': 'world', 'number': '42'}
        container = await self._create_container(bsc)
        await container.set_container_metadata(metadata)

        # Act
        props = await container.get_container_properties()

        # Assert
        self.assertIsNotNone(props)
        self.assertDictEqual(props.metadata, metadata)
        # self.assertEqual(props.lease.duration, 'infinite')
        # self.assertEqual(props.lease.state, 'leased')
        # self.assertEqual(props.lease.status, 'locked')
        # self.assertEqual(props.public_access, 'container')
        self.assertIsNotNone(props.has_immutability_policy)
        self.assertIsNotNone(props.has_legal_hold)

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    @AsyncBlobTestCase.await_prepared_test
    async def test_get_container_properties_with_lease_id(self, resource_group, location, storage_account, storage_account_key):
        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key, transport=AiohttpTestTransport())
        metadata = {'hello': 'world', 'number': '42'}
        container = await self._create_container(bsc)
        await container.set_container_metadata(metadata)
        lease_id = await container.acquire_lease()

        # Act
        props = await container.get_container_properties(lease_id)
        await lease_id.break_lease()

        # Assert
        self.assertIsNotNone(props)
        self.assertDictEqual(props.metadata, metadata)
        self.assertEqual(props.lease.duration, 'infinite')
        self.assertEqual(props.lease.state, 'leased')
        self.assertEqual(props.lease.status, 'locked')

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    @AsyncBlobTestCase.await_prepared_test
    async def test_get_container_acl(self, resource_group, location, storage_account, storage_account_key):
        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key, transport=AiohttpTestTransport())
        container = await self._create_container(bsc)

        # Act
        acl = await container.get_container_access_policy()

        # Assert
        self.assertIsNotNone(acl)
        self.assertIsNone(acl.get('public_access'))
        self.assertEqual(len(acl.get('signed_identifiers')), 0)

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    @AsyncBlobTestCase.await_prepared_test
    async def test_get_container_acl_with_lease_id(self, resource_group, location, storage_account, storage_account_key):
        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key, transport=AiohttpTestTransport())
        container = await self._create_container(bsc)
        lease_id = await container.acquire_lease()

        # Act
        acl = await container.get_container_access_policy(lease_id)

        # Assert
        self.assertIsNotNone(acl)
        self.assertIsNone(acl.get('public_access'))

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    @AsyncBlobTestCase.await_prepared_test
    async def test_set_container_acl(self, resource_group, location, storage_account, storage_account_key):
        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key, transport=AiohttpTestTransport())
        container = await self._create_container(bsc)

        # Act
        response = await container.set_container_access_policy()

        self.assertIsNotNone(response.get('etag'))
        self.assertIsNotNone(response.get('last_modified'))

        # Assert
        acl = await container.get_container_access_policy()
        self.assertIsNotNone(acl)
        self.assertEqual(len(acl.get('signed_identifiers')), 0)
        self.assertIsNone(acl.get('public_access'))

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    @AsyncBlobTestCase.await_prepared_test
    async def test_set_container_acl_with_one_signed_identifier(self, resource_group, location, storage_account, storage_account_key):
        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key, transport=AiohttpTestTransport())
        from dateutil.tz import tzutc
        container = await self._create_container(bsc)

        # Act
        access_policy = AccessPolicy(permission=ContainerPermissions.READ,
                                     expiry=datetime.utcnow() + timedelta(hours=1),
                                     start=datetime.utcnow())
        signed_identifier = {'testid': access_policy}

        response = await container.set_container_access_policy(signed_identifier)

        # Assert
        self.assertIsNotNone(response.get('etag'))
        self.assertIsNotNone(response.get('last_modified'))

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    @AsyncBlobTestCase.await_prepared_test
    async def test_set_container_acl_with_lease_id(self, resource_group, location, storage_account, storage_account_key):
        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key, transport=AiohttpTestTransport())
        container = await self._create_container(bsc)
        lease_id = await container.acquire_lease()

        # Act
        await container.set_container_access_policy(lease=lease_id)

        # Assert
        acl = await container.get_container_access_policy()
        self.assertIsNotNone(acl)
        self.assertIsNone(acl.get('public_access'))

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    @AsyncBlobTestCase.await_prepared_test
    async def test_set_container_acl_with_public_access(self, resource_group, location, storage_account, storage_account_key):
        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key, transport=AiohttpTestTransport())
        container = await self._create_container(bsc)

        # Act
        await container.set_container_access_policy(public_access='container')

        # Assert
        acl = await container.get_container_access_policy()
        self.assertIsNotNone(acl)
        self.assertEqual('container', acl.get('public_access'))

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    @AsyncBlobTestCase.await_prepared_test
    async def test_set_container_acl_with_empty_signed_identifiers(self, resource_group, location, storage_account, storage_account_key):
        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key, transport=AiohttpTestTransport())
        container = await self._create_container(bsc)

        # Act
        await container.set_container_access_policy(signed_identifiers=dict())

        # Assert
        acl = await container.get_container_access_policy()
        self.assertIsNotNone(acl)
        self.assertEqual(len(acl.get('signed_identifiers')), 0)
        self.assertIsNone(acl.get('public_access'))

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    @AsyncBlobTestCase.await_prepared_test
    async def test_set_container_acl_with_signed_identifiers(self, resource_group, location, storage_account, storage_account_key):
        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key, transport=AiohttpTestTransport())
        container = await self._create_container(bsc)

        # Act
        access_policy = AccessPolicy(permission=ContainerPermissions.READ,
                                     expiry=datetime.utcnow() + timedelta(hours=1),
                                     start=datetime.utcnow() - timedelta(minutes=1))
        identifiers = {'testid': access_policy}
        await container.set_container_access_policy(identifiers)

        # Assert
        acl = await container.get_container_access_policy()
        self.assertIsNotNone(acl)
        self.assertEqual('testid', acl.get('signed_identifiers')[0].id)
        self.assertIsNone(acl.get('public_access'))

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    @AsyncBlobTestCase.await_prepared_test
    async def test_set_container_acl_with_empty_identifiers(self, resource_group, location, storage_account, storage_account_key):
        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key, transport=AiohttpTestTransport())
        container = await self._create_container(bsc)
        identifiers = {i: None for i in range(0, 3)}

        # Act
        await container.set_container_access_policy(identifiers)

        # Assert
        acl = await container.get_container_access_policy()
        self.assertIsNotNone(acl)
        self.assertEqual(len(acl.get('signed_identifiers')), 3)
        self.assertEqual('0', acl.get('signed_identifiers')[0].id)
        self.assertIsNone(acl.get('signed_identifiers')[0].access_policy)
        self.assertIsNone(acl.get('public_access'))

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    @AsyncBlobTestCase.await_prepared_test
    async def test_set_container_acl_with_three_identifiers(self, resource_group, location, storage_account, storage_account_key):
        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key, transport=AiohttpTestTransport())
        container = await self._create_container(bsc)
        access_policy = AccessPolicy(permission=ContainerPermissions.READ,
                                     expiry=datetime.utcnow() + timedelta(hours=1),
                                     start=datetime.utcnow() - timedelta(minutes=1))
        identifiers = {i: access_policy for i in range(2)}

        # Act
        await container.set_container_access_policy(identifiers)

        # Assert
        acl = await container.get_container_access_policy()
        self.assertIsNotNone(acl)
        self.assertEqual(len(acl.get('signed_identifiers')), 2)
        self.assertEqual('0', acl.get('signed_identifiers')[0].id)
        self.assertIsNotNone(acl.get('signed_identifiers')[0].access_policy)
        self.assertIsNone(acl.get('public_access'))

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    @AsyncBlobTestCase.await_prepared_test
    async def test_set_container_acl_too_many_ids(self, resource_group, location, storage_account, storage_account_key):
        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key, transport=AiohttpTestTransport())
        container_name = await self._create_container(bsc)

        # Act
        identifiers = dict()
        for i in range(0, 6):
            identifiers['id{}'.format(i)] = AccessPolicy()

        # Assert
        with self.assertRaises(ValueError) as e:
            await container_name.set_container_access_policy(identifiers)
        self.assertEqual(
            str(e.exception),
            'Too many access policies provided. The server does not support setting more than 5 access policies on a single resource.'
        )

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    @AsyncBlobTestCase.await_prepared_test
    async def test_lease_container_acquire_and_release(self, resource_group, location, storage_account, storage_account_key):
        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key, transport=AiohttpTestTransport())
        container = await self._create_container(bsc)

        # Act
        lease = await container.acquire_lease()
        await lease.release()

        # Assert

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    @AsyncBlobTestCase.await_prepared_test
    async def test_lease_container_renew(self, resource_group, location, storage_account, storage_account_key):
        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key, transport=AiohttpTestTransport())
        container = await self._create_container(bsc)
        lease = await container.acquire_lease(lease_duration=15)
        self.sleep(10)
        lease_id_start = lease.id

        # Act
        await lease.renew()

        # Assert
        self.assertEqual(lease.id, lease_id_start)
        self.sleep(5)
        with self.assertRaises(HttpResponseError):
            await container.delete_container()
        self.sleep(10)
        await container.delete_container()

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    @AsyncBlobTestCase.await_prepared_test
    async def test_lease_container_break_period(self, resource_group, location, storage_account, storage_account_key):
        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key, transport=AiohttpTestTransport())
        container = await self._create_container(bsc)

        # Act
        lease = await container.acquire_lease(lease_duration=15)

        # Assert
        await lease.break_lease(lease_break_period=5)
        self.sleep(6)
        with self.assertRaises(HttpResponseError):
            await container.delete_container(lease=lease)

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    @AsyncBlobTestCase.await_prepared_test
    async def test_lease_container_break_released_lease_fails(self, resource_group, location, storage_account, storage_account_key):
        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key, transport=AiohttpTestTransport())
        container = await self._create_container(bsc)
        lease = await container.acquire_lease()
        await lease.release()

        # Act
        with self.assertRaises(HttpResponseError):
            await lease.break_lease()

        # Assert

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    @AsyncBlobTestCase.await_prepared_test
    async def test_lease_container_with_duration(self, resource_group, location, storage_account, storage_account_key):
        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key, transport=AiohttpTestTransport())
        container = await self._create_container(bsc)

        # Act
        lease = await container.acquire_lease(lease_duration=15)

        # Assert
        with self.assertRaises(HttpResponseError):
            await container.acquire_lease()
        self.sleep(15)
        await container.acquire_lease()

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    @AsyncBlobTestCase.await_prepared_test
    async def test_lease_container_twice(self, resource_group, location, storage_account, storage_account_key):
        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key, transport=AiohttpTestTransport())
        container = await self._create_container(bsc)

        # Act
        lease = await container.acquire_lease(lease_duration=15)

        # Assert
        lease2 = await container.acquire_lease(lease_id=lease.id)
        self.assertEqual(lease.id, lease2.id)

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    @AsyncBlobTestCase.await_prepared_test
    async def test_lease_container_with_proposed_lease_id(self, resource_group, location, storage_account, storage_account_key):
        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key, transport=AiohttpTestTransport())
        container = await self._create_container(bsc)

        # Act
        proposed_lease_id = '55e97f64-73e8-4390-838d-d9e84a374321'
        lease = await container.acquire_lease(lease_id=proposed_lease_id)

        # Assert
        self.assertEqual(proposed_lease_id, lease.id)

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    @AsyncBlobTestCase.await_prepared_test
    async def test_lease_container_change_lease_id(self, resource_group, location, storage_account, storage_account_key):
        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key, transport=AiohttpTestTransport())
        container = await self._create_container(bsc)

        # Act
        lease_id = '29e0b239-ecda-4f69-bfa3-95f6af91464c'
        lease = await container.acquire_lease()
        lease_id1 = lease.id
        await lease.change(proposed_lease_id=lease_id)
        await lease.renew()
        lease_id2 = lease.id

        # Assert
        self.assertIsNotNone(lease_id1)
        self.assertIsNotNone(lease_id2)
        self.assertNotEqual(lease_id1, lease_id)
        self.assertEqual(lease_id2, lease_id)

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    @AsyncBlobTestCase.await_prepared_test
    async def test_delete_container_with_existing_container(self, resource_group, location, storage_account, storage_account_key):
        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key, transport=AiohttpTestTransport())
        container = await self._create_container(bsc)

        # Act
        deleted = await container.delete_container()

        # Assert
        self.assertIsNone(deleted)

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    @AsyncBlobTestCase.await_prepared_test
    async def test_delete_container_with_non_existing_container_fail_not_exist(self, resource_group, location, storage_account, storage_account_key):
        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key, transport=AiohttpTestTransport())
        container_name = self._get_container_reference()
        container = bsc.get_container_client(container_name)

        # Act
        with LogCaptured(self) as log_captured:
            with self.assertRaises(ResourceNotFoundError):
                await container.delete_container()

            log_as_str = log_captured.getvalue()
            #self.assertTrue('ERROR' in log_as_str)

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    @AsyncBlobTestCase.await_prepared_test
    async def test_delete_container_with_lease_id(self, resource_group, location, storage_account, storage_account_key):
        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key, transport=AiohttpTestTransport())
        container = await self._create_container(bsc)
        lease = await container.acquire_lease(lease_duration=15)

        # Act
        deleted = await container.delete_container(lease=lease)

        # Assert
        self.assertIsNone(deleted)
        with self.assertRaises(ResourceNotFoundError):
            await container.get_container_properties()

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    @AsyncBlobTestCase.await_prepared_test
    async def test_list_names(self, resource_group, location, storage_account, storage_account_key):
        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key, transport=AiohttpTestTransport())
        container = await self._create_container(bsc)
        data = b'hello world'

        await (container.get_blob_client('blob1')).upload_blob(data)
        await (container.get_blob_client('blob2')).upload_blob(data)


        # Act
        blobs = []
        async for b in container.list_blobs():
            blobs.append(b.name)

        self.assertEqual(blobs, ['blob1', 'blob2'])

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    @AsyncBlobTestCase.await_prepared_test
    async def test_list_blobs(self, resource_group, location, storage_account, storage_account_key):
        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key, transport=AiohttpTestTransport())
        container = await self._create_container(bsc)
        data = b'hello world'
        cr0 = container.get_blob_client('blob1')
        await cr0.upload_blob(data)
        cr1 = container.get_blob_client('blob2')
        await cr1.upload_blob(data)

        # Act
        blobs = []
        async for b in container.list_blobs():
            blobs.append(b)

        # Assert
        self.assertIsNotNone(blobs)
        self.assertGreaterEqual(len(blobs), 2)
        self.assertIsNotNone(blobs[0])
        self.assert_named_item_in_container(blobs, 'blob1')
        self.assert_named_item_in_container(blobs, 'blob2')
        self.assertEqual(blobs[0].size, 11)
        self.assertEqual(blobs[1].content_settings.content_type,
                         'application/octet-stream')
        self.assertIsNotNone(blobs[0].creation_time)

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    @AsyncBlobTestCase.await_prepared_test
    async def test_list_blobs_leased_blob(self, resource_group, location, storage_account, storage_account_key):
        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key, transport=AiohttpTestTransport())
        container = await self._create_container(bsc)
        data = b'hello world'
        blob1 = container.get_blob_client('blob1')
        await blob1.upload_blob(data)
        lease = await blob1.acquire_lease()

        # Act
        resp = []
        async for b in container.list_blobs():
            resp.append(b)
        # Assert
        self.assertIsNotNone(resp)
        self.assertGreaterEqual(len(resp), 1)
        self.assertIsNotNone(resp[0])
        self.assert_named_item_in_container(resp, 'blob1')
        self.assertEqual(resp[0].size, 11)
        self.assertEqual(resp[0].lease.duration, 'infinite')
        self.assertEqual(resp[0].lease.status, 'locked')
        self.assertEqual(resp[0].lease.state, 'leased')

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    @AsyncBlobTestCase.await_prepared_test
    async def test_list_blobs_with_prefix(self, resource_group, location, storage_account, storage_account_key):
        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key, transport=AiohttpTestTransport())
        container = await self._create_container(bsc)
        data = b'hello world'
        c0 = container.get_blob_client('blob_a1')
        await c0.upload_blob(data)
        c1 = container.get_blob_client('blob_a2')
        await c1.upload_blob(data)
        c2 = container.get_blob_client('blob_b1')
        await c2.upload_blob(data)

        # Act
        resp = []
        async for b in container.list_blobs(name_starts_with='blob_a'):
            resp.append(b)

        # Assert
        self.assertIsNotNone(resp)
        self.assertEqual(len(resp), 2)
        self.assert_named_item_in_container(resp, 'blob_a1')
        self.assert_named_item_in_container(resp, 'blob_a2')

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    @AsyncBlobTestCase.await_prepared_test
    async def test_list_blobs_with_num_results(self, resource_group, location, storage_account, storage_account_key):
        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key, transport=AiohttpTestTransport())
        container = await self._create_container(bsc)
        data = b'hello world'
        c0 = container.get_blob_client('blob_a1')
        await c0.upload_blob(data)
        c1 = container.get_blob_client('blob_a2')
        await c1.upload_blob(data)
        c2 = container.get_blob_client('blob_a3')
        await c2.upload_blob(data)
        c3 = container.get_blob_client('blob_b1')
        await c3.upload_blob(data)

        # Act
        generator = container.list_blobs(results_per_page=2).by_page()
        blobs = []
        async for b in await generator.__anext__():
            blobs.append(b)

        # Assert
        self.assertIsNotNone(blobs)
        self.assertEqual(len(blobs), 2)
        self.assert_named_item_in_container(generator.current_page, 'blob_a1')
        self.assert_named_item_in_container(generator.current_page, 'blob_a2')

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    @AsyncBlobTestCase.await_prepared_test
    async def test_list_blobs_with_include_snapshots(self, resource_group, location, storage_account, storage_account_key):
        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key, transport=AiohttpTestTransport())
        container = await self._create_container(bsc)
        data = b'hello world'
        blob1 = container.get_blob_client('blob1')
        await blob1.upload_blob(data)
        await blob1.create_snapshot()
        await (container.get_blob_client('blob2')).upload_blob(data)

        # Act
        blobs = []
        async for b in container.list_blobs(include="snapshots"):
            blobs.append(b)

        # Assert
        self.assertEqual(len(blobs), 3)
        self.assertEqual(blobs[0].name, 'blob1')
        self.assertIsNotNone(blobs[0].snapshot)
        self.assertEqual(blobs[1].name, 'blob1')
        self.assertIsNone(blobs[1].snapshot)
        self.assertEqual(blobs[2].name, 'blob2')
        self.assertIsNone(blobs[2].snapshot)

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    @AsyncBlobTestCase.await_prepared_test
    async def test_list_blobs_with_include_metadata(self, resource_group, location, storage_account, storage_account_key):
        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key, transport=AiohttpTestTransport())
        pytest.skip("Waiting on metadata XML fix in msrest")
        container = await self._create_container(bsc)
        data = b'hello world'
        blob1 = container.get_blob_client('blob1')
        await blob1.upload_blob(data, metadata={'number': '1', 'name': 'bob'})
        await blob1.create_snapshot()
        cr = container.get_blob_client('blob2')
        await cr.upload_blob(data, metadata={'number': '2', 'name': 'car'})

        # Act
        blobs = []
        async for b in container.list_blobs(include="metadata"):
            blobs.append(b)

        # Assert
        self.assertEqual(len(blobs), 2)
        self.assertEqual(blobs[0].name, 'blob1')
        self.assertEqual(blobs[0].metadata['number'], '1')
        self.assertEqual(blobs[0].metadata['name'], 'bob')
        self.assertEqual(blobs[1].name, 'blob2')
        self.assertEqual(blobs[1].metadata['number'], '2')
        self.assertEqual(blobs[1].metadata['name'], 'car')

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    @AsyncBlobTestCase.await_prepared_test
    async def test_list_blobs_with_include_uncommittedblobs(self, resource_group, location, storage_account, storage_account_key):
        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key, transport=AiohttpTestTransport())
        container = await self._create_container(bsc)
        data = b'hello world'
        blob1 = container.get_blob_client('blob1')
        await blob1.stage_block('1', b'AAA')
        await blob1.stage_block('2', b'BBB')
        await blob1.stage_block('3', b'CCC')

        blob2 = container.get_blob_client('blob2')
        await blob2.upload_blob(data, metadata={'number': '2', 'name': 'car'})

        # Act
        blobs = []
        async for b in container.list_blobs(include="uncommittedblobs"):
            blobs.append(b)

        # Assert
        self.assertEqual(len(blobs), 2)
        self.assertEqual(blobs[0].name, 'blob1')
        self.assertEqual(blobs[1].name, 'blob2')

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    @AsyncBlobTestCase.await_prepared_test
    async def test_list_blobs_with_include_copy(self, resource_group, location, storage_account, storage_account_key):
        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key, transport=AiohttpTestTransport())
        container = await self._create_container(bsc)
        data = b'hello world'
        await (container.get_blob_client('blob1')).upload_blob(data, metadata={'status': 'original'})
        sourceblob = 'https://{0}.blob.core.windows.net/{1}/blob1'.format(
        storage_account.name,
            container.container_name)

        blobcopy = container.get_blob_client('blob1copy')
        await blobcopy.start_copy_from_url(sourceblob, metadata={'status': 'copy'})

        # Act
        blobs = []
        async for b in container.list_blobs(include="copy"):
            blobs.append(b)

        # Assert
        self.assertEqual(len(blobs), 2)
        self.assertEqual(blobs[0].name, 'blob1')
        self.assertEqual(blobs[1].name, 'blob1copy')
        self.assertEqual(blobs[1].blob_type, blobs[0].blob_type)
        self.assertEqual(blobs[1].size, 11)
        self.assertEqual(blobs[1].content_settings.content_type,
                         'application/octet-stream')
        self.assertEqual(blobs[1].content_settings.cache_control, None)
        self.assertEqual(blobs[1].content_settings.content_encoding, None)
        self.assertEqual(blobs[1].content_settings.content_language, None)
        self.assertEqual(blobs[1].content_settings.content_disposition, None)
        self.assertNotEqual(blobs[1].content_settings.content_md5, None)
        self.assertEqual(blobs[1].lease.status, 'unlocked')
        self.assertEqual(blobs[1].lease.state, 'available')
        self.assertNotEqual(blobs[1].copy.id, None)
        self.assertEqual(blobs[1].copy.source, sourceblob)
        self.assertEqual(blobs[1].copy.status, 'success')
        self.assertEqual(blobs[1].copy.progress, '11/11')
        self.assertNotEqual(blobs[1].copy.completion_time, None)

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    @AsyncBlobTestCase.await_prepared_test
    async def test_list_blobs_with_delimiter(self, resource_group, location, storage_account, storage_account_key):
        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key, transport=AiohttpTestTransport())
        container = await self._create_container(bsc)
        data = b'hello world'

        cr0 = container.get_blob_client('a/blob1')
        await cr0.upload_blob(data)
        cr1 = container.get_blob_client('a/blob2')
        await cr1.upload_blob(data)
        cr2 = container.get_blob_client('b/blob3')
        await cr2.upload_blob(data)
        cr4 = container.get_blob_client('blob4')
        await cr4.upload_blob(data)

        # Act
        resp = []
        async for w in container.walk_blobs():
            resp.append(w)

        # Assert
        self.assertIsNotNone(resp)
        self.assertEqual(len(resp), 3)
        self.assert_named_item_in_container(resp, 'a/')
        self.assert_named_item_in_container(resp, 'b/')
        self.assert_named_item_in_container(resp, 'blob4')

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    @AsyncBlobTestCase.await_prepared_test
    async def test_walk_blobs_with_delimiter(self, resource_group, location, storage_account, storage_account_key):
        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key, transport=AiohttpTestTransport())
        container = await self._create_container(bsc)
        data = b'hello world'

        cr0 = container.get_blob_client('a/blob1')
        await cr0.upload_blob(data)
        cr1 = container.get_blob_client('a/blob2')
        await cr1.upload_blob(data)
        cr2 = container.get_blob_client('b/c/blob3')
        await cr2.upload_blob(data)
        cr3 = container.get_blob_client('blob4')
        await cr3.upload_blob(data)

        blob_list = []
        def recursive_walk(prefix):
            for b in prefix:
                if b.get('prefix'):
                    recursive_walk(b)
                else:
                    blob_list.append(b.name)

        # Act
        recursive_walk(container.walk_blobs())

        # Assert
        self.assertEqual(len(blob_list), 4)
        self.assertEqual(blob_list, ['a/blob1', 'a/blob2', 'b/c/blob3', 'blob4'])

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    @AsyncBlobTestCase.await_prepared_test
    async def test_list_blobs_with_include_multiple(self, resource_group, location, storage_account, storage_account_key):
        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key, transport=AiohttpTestTransport())
        pytest.skip("Waiting on metadata XML fix in msrest")
        container = await self._create_container(bsc)
        data = b'hello world'
        blob1 = container.get_blob_client('blob1')
        await blob1.upload_blob(data, metadata={'number': '1', 'name': 'bob'})
        await blob1.create_snapshot()

        client = container.get_blob_client('blob2')
        await client.upload_blob(data, metadata={'number': '2', 'name': 'car'})

        # Act
        blobs = []
        async for b in container.list_blobs(include=["snapshots", "metadata"]):
            blobs.append(b)

        # Assert
        self.assertEqual(len(blobs), 3)
        self.assertEqual(blobs[0].name, 'blob1')
        self.assertIsNotNone(blobs[0].snapshot)
        self.assertEqual(blobs[0].metadata['number'], '1')
        self.assertEqual(blobs[0].metadata['name'], 'bob')
        self.assertEqual(blobs[1].name, 'blob1')
        self.assertIsNone(blobs[1].snapshot)
        self.assertEqual(blobs[1].metadata['number'], '1')
        self.assertEqual(blobs[1].metadata['name'], 'bob')
        self.assertEqual(blobs[2].name, 'blob2')
        self.assertIsNone(blobs[2].snapshot)
        self.assertEqual(blobs[2].metadata['number'], '2')
        self.assertEqual(blobs[2].metadata['name'], 'car')

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    @AsyncBlobTestCase.await_prepared_test
    async def test_shared_access_container(self, resource_group, location, storage_account, storage_account_key):
        # SAS URL is calculated from storage key, so this test runs live only
        if not self.is_live:
            return

        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key, transport=AiohttpTestTransport())
        container = await self._create_container(bsc)
        blob_name  = 'blob1'
        data = b'hello world'

        blob = container.get_blob_client(blob_name)
        await blob.upload_blob(data)

        token = container.generate_shared_access_signature(
            expiry=datetime.utcnow() + timedelta(hours=1),
            permission=ContainerPermissions.READ,
        )
        blob = BlobClient(blob.url, credential=token)

        # Act
        response = requests.get(blob.url)

        # Assert
        self.assertTrue(response.ok)
        self.assertEqual(data, response.content)

    @ResourceGroupPreparer()
    @StorageAccountPreparer(name_prefix='pyacrstorage')
    @AsyncBlobTestCase.await_prepared_test
    async def test_web_container_normal_operations_working(self, resource_group, location, storage_account, storage_account_key):
        web_container = "web"
        bsc = BlobServiceClient(self._account_url(storage_account.name), storage_account_key, transport=AiohttpTestTransport())

        # create the web container in case it does not exist yet
        container = bsc.get_container_client(web_container)
        try:
            try:
                created = await container.create_container()
                self.assertIsNotNone(created)
            except ResourceExistsError:
                pass

            # test if web container exists
            exist = await container.get_container_properties()
            self.assertTrue(exist)

            # create a blob
            blob_name = self.get_resource_name("blob")
            blob_content = self.get_random_text_data(1024)
            blob = container.get_blob_client(blob_name)
            await blob.upload_blob(blob_content)

            # get a blob
            blob_data = await (await blob.download_blob()).content_as_bytes()
            self.assertIsNotNone(blob)
            self.assertEqual(blob_data.decode('utf-8'), blob_content)

        finally:
            # delete container
            await container.delete_container()

#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
