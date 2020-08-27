# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class AnomalyDetectorClientOperationsMixin:

    async def detect_entire_series(
        self,
        body: "models.DetectRequest",
        **kwargs
    ) -> "models.EntireDetectResponse":
        """Detect anomalies for the entire series in batch.

        This operation generates a model using an entire series, each point is detected with the same
        model. With this method, points before and after a certain point are used to determine whether
        it is an anomaly. The entire detection can give user an overall status of the time series.

        :param body: Time series points and period if needed. Advanced model parameters can also be set
         in the request.
        :type body: ~azure.ai.anomalydetector.models.DetectRequest
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: EntireDetectResponse, or the result of cls(response)
        :rtype: ~azure.ai.anomalydetector.models.EntireDetectResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.EntireDetectResponse"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.detect_entire_series.metadata['url']  # type: ignore
        path_format_arguments = {
            'Endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'DetectRequest')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.AnomalyDetectorError, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('EntireDetectResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    detect_entire_series.metadata = {'url': '/timeseries/entire/detect'}  # type: ignore

    async def detect_last_point(
        self,
        body: "models.DetectRequest",
        **kwargs
    ) -> "models.LastDetectResponse":
        """Detect anomaly status of the latest point in time series.

        This operation generates a model using points before the latest one. With this method, only
        historical points are used to determine whether the target point is an anomaly. The latest
        point detecting operation matches the scenario of real-time monitoring of business metrics.

        :param body: Time series points and period if needed. Advanced model parameters can also be set
         in the request.
        :type body: ~azure.ai.anomalydetector.models.DetectRequest
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: LastDetectResponse, or the result of cls(response)
        :rtype: ~azure.ai.anomalydetector.models.LastDetectResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.LastDetectResponse"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.detect_last_point.metadata['url']  # type: ignore
        path_format_arguments = {
            'Endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'DetectRequest')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.AnomalyDetectorError, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('LastDetectResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    detect_last_point.metadata = {'url': '/timeseries/last/detect'}  # type: ignore

    async def detect_change_point(
        self,
        body: "models.ChangePointDetectRequest",
        **kwargs
    ) -> "models.ChangePointDetectResponse":
        """Detect change point for the entire series.

        Evaluate change point score of every series point.

        :param body: Time series points and granularity is needed. Advanced model parameters can also
         be set in the request if needed.
        :type body: ~azure.ai.anomalydetector.models.ChangePointDetectRequest
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ChangePointDetectResponse, or the result of cls(response)
        :rtype: ~azure.ai.anomalydetector.models.ChangePointDetectResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ChangePointDetectResponse"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.detect_change_point.metadata['url']  # type: ignore
        path_format_arguments = {
            'Endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'ChangePointDetectRequest')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.AnomalyDetectorError, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('ChangePointDetectResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    detect_change_point.metadata = {'url': '/timeseries/changepoint/detect'}  # type: ignore
