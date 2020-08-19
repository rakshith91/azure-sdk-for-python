# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any

from azure.core import AsyncPipelineClient
from msrest import Deserializer, Serializer

from ._configuration_async import AzureTableConfiguration
from .operations_async import TableOperations
from .operations_async import ServiceOperations
from .. import models


class AzureTable(object):
    """AzureTable.

    :ivar table: TableOperations operations
    :vartype table: azure.data.tables.aio.operations_async.TableOperations
    :ivar service: ServiceOperations operations
    :vartype service: azure.data.tables.aio.operations_async.ServiceOperations
    :param url: The URL of the service account or table that is the target of the desired operation.
    :type url: str
    """

    def __init__(
        self,
        url: str,
        **kwargs: Any
    ) -> None:
        base_url = '{url}'
        self._config = AzureTableConfiguration(url, **kwargs)
        self._client = AsyncPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.table = TableOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.service = ServiceOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "AzureTable":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
