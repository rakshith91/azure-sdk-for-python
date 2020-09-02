# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING
import json
import six
import logging

from azure.core import PipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any

_LOGGER = logging.getLogger(__name__)

from ._models import CloudEvent, EventGridEvent

class EventGridConsumer(object):
    """
    A consumer responsible for deserializing event handler messages, to allow for access to strongly typed Event objects.
    """
    def decode_cloud_event(self, cloud_event, **kwargs):
        # type: (Union[str, dict, bytes], Any) -> CloudEvent
        """Single event following CloudEvent schema will be parsed and returned as Deserialized Event.
        :param cloud_event: The event to be deserialized.
        :type cloud_event: Union[str, dict, bytes]
        :rtype: CloudEvent

        :raise: :class:`ValueError`, when events do not follow CloudEvent schema.
        """
        encode = kwargs.pop('encoding', 'utf-8')
        try:
            cloud_event = CloudEvent._load(cloud_event, encode)
            deserialized_event = CloudEvent.deserialize(cloud_event)
            CloudEvent._deserialize_data(deserialized_event, deserialized_event.type)
            return deserialized_event 
        except Exception as err:
            _LOGGER.error('Error: cannot deserialize event. Event does not have a valid format. Event must be a string, dict, or bytes following the CloudEvent schema.')
            _LOGGER.error('Your event: {}'.format(cloud_event))
            _LOGGER.error(err)
            raise ValueError('Error: cannot deserialize event. Event does not have a valid format. Event must be a string, dict, or bytes following the CloudEvent schema.') 

    def decode_eventgrid_event(self, eventgrid_event, **kwargs):
        # type: (Union[str, dict, bytes], Any) -> EventGridEvent
        """Single event following EventGridEvent schema will be parsed and returned as Deserialized Event.
        :param eventgrid_event: The event to be deserialized.
        :type eventgrid_event: Union[str, dict, bytes]
        :rtype: EventGridEvent

        :raise: :class:`ValueError`, when events do not follow EventGridEvent schema.
        """
        encode = kwargs.pop('encoding', 'utf-8')
        try:
            eventgrid_event = EventGridEvent._load(eventgrid_event, encode)
            deserialized_event = EventGridEvent.deserialize(eventgrid_event)
            EventGridEvent._deserialize_data(deserialized_event, deserialized_event.event_type)
            return deserialized_event
        except Exception as err:
            _LOGGER.error('Error: cannot deserialize event. Event does not have a valid format. Event must be a string, dict, or bytes following the CloudEvent schema.')
            _LOGGER.error('Your event: {}'.format(eventgrid_event))
            _LOGGER.error(err)
            raise ValueError('Error: cannot deserialize event. Event does not have a valid format. Event must be a string, dict, or bytes following the CloudEvent schema.') 
