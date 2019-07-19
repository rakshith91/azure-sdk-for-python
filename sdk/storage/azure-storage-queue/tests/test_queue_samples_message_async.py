# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

import pytest
import asyncio
from datetime import datetime, timedelta

try:
    import settings_real as settings
except ImportError:
    import queue_settings_fake as settings

from queuetestcase import (
    QueueTestCase,
    record,
    TestMode
)


class TestMessageQueueSamplesAsync(QueueTestCase):

    connection_string = settings.CONNECTION_STRING
    storage_url = "{}://{}.queue.core.windows.net".format(
        settings.PROTOCOL,
        settings.STORAGE_ACCOUNT_NAME
    )

    async def _test_set_access_policy(self):
        # SAS URL is calculated from storage key, so this test runs live only
        if TestMode.need_recording_file(self.test_mode):
            return

        # [START create_queue_client_from_connection_string]
        from azure.storage.queue.aio import QueueClient
        queue_client = QueueClient.from_connection_string(self.connection_string, "queuetest")
        # [END create_queue_client_from_connection_string]

        # Create the queue
        queue_client.create_queue()
        await queue_client.enqueue_message('hello world')

        try:
            # [START set_access_policy]
            # Create an access policy
            from azure.storage.queue import AccessPolicy, QueuePermissions
            access_policy = AccessPolicy()
            access_policy.start = datetime.utcnow() - timedelta(hours=1)
            access_policy.expiry = datetime.utcnow() + timedelta(hours=1)
            access_policy.permission = QueuePermissions.READ
            identifiers = {'my-access-policy-id': access_policy}

            # Set the access policy
            await queue_client.set_queue_access_policy(identifiers)
            # [END set_access_policy]

            # Use the access policy to generate a SAS token
            # [START queue_client_sas_token]
            sas_token = await queue_client.generate_shared_access_signature(
                policy_id='my-access-policy-id'
            )
            # [END queue_client_sas_token]

            # Authenticate with the sas token
            # [START create_queue_client]
            q = QueueClient(
                queue_url=queue_client.url,
                credential=sas_token
            )
            # [END create_queue_client]

            # Use the newly authenticated client to receive messages
            my_message = q.receive_messages()
            assert my_message is not None

        finally:
            # Delete the queue
            await queue_client.delete_queue()

    def test_set_access_policy(self):
        if TestMode.need_recording_file(self.test_mode):
            return
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self._test_set_access_policy())

    async def _test_queue_metadata(self):

        # Instantiate a queue client
        from azure.storage.queue.aio import QueueClient
        queue = QueueClient.from_connection_string(self.connection_string, "metaqueue")

        # Create the queue
        queue.create_queue()

        try:
            # [START set_queue_metadata]
            metadata = {'foo': 'val1', 'bar': 'val2', 'baz': 'val3'}
            await queue.set_queue_metadata(metadata=metadata)
            # [END set_queue_metadata]

            # [START get_queue_properties]
            response = await queue.get_queue_properties().metadata
            # [END get_queue_properties]
            assert response == metadata

        finally:
            # Delete the queue
            await queue.delete_queue()

    def test_queue_metadata(self):
        if TestMode.need_recording_file(self.test_mode):
            return
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self._test_queue_metadata())

    async def _test_enqueue_and_receive_messages(self):

        # Instantiate a queue client
        from azure.storage.queue.aio import QueueClient
        queue = QueueClient.from_connection_string(self.connection_string, "messagequeue")

        # Create the queue
        queue.create_queue()

        try:
            # [START enqueue_messages]
            await queue.enqueue_message(u"message1")
            await queue.enqueue_message(u"message2", visibility_timeout=30)  # wait 30s before becoming visible
            await queue.enqueue_message(u"message3")
            await queue.enqueue_message(u"message4")
            await queue.enqueue_message(u"message5")
            # [END enqueue_messages]

            # [START receive_messages]
            # receive one message from the front of the queue
            one_msg = await queue.receive_messages()

            # Receive the last 5 messages
            messages = await queue.receive_messages(messages_per_page=5)

            # Print the messages
            for msg in messages:
                print(msg.content)
            # [END receive_messages]

            # Only prints 4 messages because message 2 is not visible yet
            # >>message1
            # >>message3
            # >>message4
            # >>message5

        finally:
            # Delete the queue
            await queue.delete_queue()

    def test_enqueue_and_receive_messages(self):
        if TestMode.need_recording_file(self.test_mode):
            return
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self._test_enqueue_and_receive_messages())

    async def _test_delete_and_clear_messages(self):

        # Instantiate a queue client
        from azure.storage.queue.aio import QueueClient
        queue = QueueClient.from_connection_string(self.connection_string, "delqueue")

        # Create the queue
        queue.create_queue()

        try:
            # Enqueue messages
            await queue.enqueue_message(u"message1")
            await queue.enqueue_message(u"message2")
            await queue.enqueue_message(u"message3")
            await queue.enqueue_message(u"message4")
            await queue.enqueue_message(u"message5")

            # [START delete_message]
            # Get the message at the front of the queue
            msg = await next(queue.receive_messages())

            # Delete the specified message
            await queue.delete_message(msg)
            # [END delete_message]

            # [START clear_messages]
            await queue.clear_messages()
            # [END clear_messages]

        finally:
            # Delete the queue
            await queue.delete_queue()

    def test_delete_and_clear_messages(self):
        if TestMode.need_recording_file(self.test_mode):
            return
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self._test_delete_and_clear_messages())

    async def _test_peek_messages(self):
        # Instantiate a queue client
        from azure.storage.queue.aio import QueueClient
        queue = QueueClient.from_connection_string(self.connection_string, "peekqueue")

        # Create the queue
        queue.create_queue()

        try:
            # Enqueue messages
            await queue.enqueue_message(u"message1")
            await queue.enqueue_message(u"message2")
            await queue.enqueue_message(u"message3")
            await queue.enqueue_message(u"message4")
            await queue.enqueue_message(u"message5")

            # [START peek_message]
            # Peek at one message at the front of the queue
            msg = await queue.peek_messages()

            # Peek at the last 5 messages
            messages = await queue.peek_messages(max_messages=5)

            # Print the last 5 messages
            for message in messages:
                print(message.content)
            # [END peek_message]

        finally:
            # Delete the queue
            await queue.delete_queue()

    def test_peek_messages(self):
        if TestMode.need_recording_file(self.test_mode):
            return
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self._test_peek_messages())

    async def _test_update_message(self):

        # Instantiate a queue client
        from azure.storage.queue.aio import QueueClient
        queue = QueueClient.from_connection_string(self.connection_string, "updatequeue")

        # Create the queue
        queue.create_queue()

        try:
            # [START update_message]
            # Enqueue a message
            await queue.enqueue_message(u"update me")

            # Receive the message
            messages = await queue.receive_messages()

            # Update the message
            list_result = next(messages)
            message = await queue.update_message(
                list_result.id,
                pop_receipt=list_result.pop_receipt,
                visibility_timeout=0,
                content=u"updated")
            # [END update_message]
            assert message.content == "updated"

        finally:
            # Delete the queue
            await queue.delete_queue()

    def test_update_message(self):
            if TestMode.need_recording_file(self.test_mode):
                return
            loop = asyncio.get_event_loop()
            loop.run_until_complete(self._test_update_message())
