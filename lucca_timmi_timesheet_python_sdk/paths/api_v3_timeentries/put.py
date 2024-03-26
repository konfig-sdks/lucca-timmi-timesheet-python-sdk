# coding: utf-8

"""
    Timmi Timesheet API

    Welcome on the documentation for the Timmi Timesheet API. 

    The version of the OpenAPI document: 1.0
    Contact: developers@lucca.fr
    Created by: https://www.lucca.fr
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from lucca_timmi_timesheet_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from lucca_timmi_timesheet_python_sdk.api_response import AsyncGeneratorResponse
from lucca_timmi_timesheet_python_sdk import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from lucca_timmi_timesheet_python_sdk import schemas  # noqa: F401

from lucca_timmi_timesheet_python_sdk.model.time_entries_update_multiple_request import TimeEntriesUpdateMultipleRequest as TimeEntriesUpdateMultipleRequestSchema
from lucca_timmi_timesheet_python_sdk.model.time_entries_update_multiple_response import TimeEntriesUpdateMultipleResponse as TimeEntriesUpdateMultipleResponseSchema
from lucca_timmi_timesheet_python_sdk.model.time_entries_delete_multiple_response import TimeEntriesDeleteMultipleResponse as TimeEntriesDeleteMultipleResponseSchema
from lucca_timmi_timesheet_python_sdk.model.axis_section import AxisSection as AxisSectionSchema

from lucca_timmi_timesheet_python_sdk.type.time_entries_update_multiple_response import TimeEntriesUpdateMultipleResponse
from lucca_timmi_timesheet_python_sdk.type.time_entries_delete_multiple_response import TimeEntriesDeleteMultipleResponse
from lucca_timmi_timesheet_python_sdk.type.time_entries_update_multiple_request import TimeEntriesUpdateMultipleRequest
from lucca_timmi_timesheet_python_sdk.type.axis_section import AxisSection

from ...api_client import Dictionary
from lucca_timmi_timesheet_python_sdk.pydantic.time_entries_update_multiple_request import TimeEntriesUpdateMultipleRequest as TimeEntriesUpdateMultipleRequestPydantic
from lucca_timmi_timesheet_python_sdk.pydantic.time_entries_update_multiple_response import TimeEntriesUpdateMultipleResponse as TimeEntriesUpdateMultipleResponsePydantic
from lucca_timmi_timesheet_python_sdk.pydantic.time_entries_delete_multiple_response import TimeEntriesDeleteMultipleResponse as TimeEntriesDeleteMultipleResponsePydantic
from lucca_timmi_timesheet_python_sdk.pydantic.axis_section import AxisSection as AxisSectionPydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = TimeEntriesUpdateMultipleRequestSchema


request_body_time_entries_update_multiple_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
_auth = [
    'Authorization',
]
SchemaFor200ResponseBodyApplicationJson = TimeEntriesUpdateMultipleResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: TimeEntriesUpdateMultipleResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: TimeEntriesUpdateMultipleResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = TimeEntriesDeleteMultipleResponseSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: TimeEntriesDeleteMultipleResponse


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: TimeEntriesDeleteMultipleResponse


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor401ResponseBodyApplicationJson = TimeEntriesDeleteMultipleResponseSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: TimeEntriesDeleteMultipleResponse


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: TimeEntriesDeleteMultipleResponse


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)
SchemaFor403ResponseBodyApplicationJson = TimeEntriesDeleteMultipleResponseSchema


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: TimeEntriesDeleteMultipleResponse


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: TimeEntriesDeleteMultipleResponse


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationJson),
    },
)
SchemaFor500ResponseBodyApplicationJson = TimeEntriesDeleteMultipleResponseSchema


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: TimeEntriesDeleteMultipleResponse


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: TimeEntriesDeleteMultipleResponse


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    response_cls_async=ApiResponseFor500Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '401': _response_for_401,
    '403': _response_for_403,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _update_multiple_mapped_args(
        self,
        id: typing.Optional[int] = None,
        starts_at: typing.Optional[datetime] = None,
        duration: typing.Optional[str] = None,
        unit: typing.Optional[int] = None,
        ends_at: typing.Optional[datetime] = None,
        owner_id: typing.Optional[int] = None,
        author_id: typing.Optional[int] = None,
        created_at: typing.Optional[datetime] = None,
        creation_source: typing.Optional[int] = None,
        modifier_id: typing.Optional[int] = None,
        modified_at: typing.Optional[int] = None,
        layer: typing.Optional[int] = None,
        axis_sections: typing.Optional[typing.List[AxisSection]] = None,
        comment: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        time_type_id: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        body: typing.Optional[TimeEntriesUpdateMultipleRequest] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if id is not None:
            _body["id"] = id
        if starts_at is not None:
            _body["startsAt"] = starts_at
        if duration is not None:
            _body["duration"] = duration
        if unit is not None:
            _body["unit"] = unit
        if ends_at is not None:
            _body["endsAt"] = ends_at
        if owner_id is not None:
            _body["ownerId"] = owner_id
        if author_id is not None:
            _body["authorId"] = author_id
        if created_at is not None:
            _body["createdAt"] = created_at
        if creation_source is not None:
            _body["creationSource"] = creation_source
        if modifier_id is not None:
            _body["modifierId"] = modifier_id
        if modified_at is not None:
            _body["modifiedAt"] = modified_at
        if layer is not None:
            _body["layer"] = layer
        if axis_sections is not None:
            _body["axisSections"] = axis_sections
        if comment is not None:
            _body["comment"] = comment
        if time_type_id is not None:
            _body["timeTypeId"] = time_type_id
        args.body = body if body is not None else _body
        return args

    async def _aupdate_multiple_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Update multiple TimeEntries
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'put'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v3/timeentries',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_time_entries_update_multiple_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _update_multiple_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Update multiple TimeEntries
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'put'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v3/timeentries',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_time_entries_update_multiple_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class UpdateMultipleRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @api_client.DeprecationWarningOnce(prefix="time_entries")
    async def aupdate_multiple(
        self,
        id: typing.Optional[int] = None,
        starts_at: typing.Optional[datetime] = None,
        duration: typing.Optional[str] = None,
        unit: typing.Optional[int] = None,
        ends_at: typing.Optional[datetime] = None,
        owner_id: typing.Optional[int] = None,
        author_id: typing.Optional[int] = None,
        created_at: typing.Optional[datetime] = None,
        creation_source: typing.Optional[int] = None,
        modifier_id: typing.Optional[int] = None,
        modified_at: typing.Optional[int] = None,
        layer: typing.Optional[int] = None,
        axis_sections: typing.Optional[typing.List[AxisSection]] = None,
        comment: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        time_type_id: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        body: typing.Optional[TimeEntriesUpdateMultipleRequest] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_multiple_mapped_args(
            body=body,
            id=id,
            starts_at=starts_at,
            duration=duration,
            unit=unit,
            ends_at=ends_at,
            owner_id=owner_id,
            author_id=author_id,
            created_at=created_at,
            creation_source=creation_source,
            modifier_id=modifier_id,
            modified_at=modified_at,
            layer=layer,
            axis_sections=axis_sections,
            comment=comment,
            time_type_id=time_type_id,
        )
        return await self._aupdate_multiple_oapg(
            body=args.body,
            **kwargs,
        )
    
    @api_client.DeprecationWarningOnce(prefix="time_entries")
    def update_multiple(
        self,
        id: typing.Optional[int] = None,
        starts_at: typing.Optional[datetime] = None,
        duration: typing.Optional[str] = None,
        unit: typing.Optional[int] = None,
        ends_at: typing.Optional[datetime] = None,
        owner_id: typing.Optional[int] = None,
        author_id: typing.Optional[int] = None,
        created_at: typing.Optional[datetime] = None,
        creation_source: typing.Optional[int] = None,
        modifier_id: typing.Optional[int] = None,
        modified_at: typing.Optional[int] = None,
        layer: typing.Optional[int] = None,
        axis_sections: typing.Optional[typing.List[AxisSection]] = None,
        comment: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        time_type_id: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        body: typing.Optional[TimeEntriesUpdateMultipleRequest] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_multiple_mapped_args(
            body=body,
            id=id,
            starts_at=starts_at,
            duration=duration,
            unit=unit,
            ends_at=ends_at,
            owner_id=owner_id,
            author_id=author_id,
            created_at=created_at,
            creation_source=creation_source,
            modifier_id=modifier_id,
            modified_at=modified_at,
            layer=layer,
            axis_sections=axis_sections,
            comment=comment,
            time_type_id=time_type_id,
        )
        return self._update_multiple_oapg(
            body=args.body,
        )

class UpdateMultiple(BaseApi):

    @api_client.DeprecationWarningOnce(prefix="time_entries")
    async def aupdate_multiple(
        self,
        id: typing.Optional[int] = None,
        starts_at: typing.Optional[datetime] = None,
        duration: typing.Optional[str] = None,
        unit: typing.Optional[int] = None,
        ends_at: typing.Optional[datetime] = None,
        owner_id: typing.Optional[int] = None,
        author_id: typing.Optional[int] = None,
        created_at: typing.Optional[datetime] = None,
        creation_source: typing.Optional[int] = None,
        modifier_id: typing.Optional[int] = None,
        modified_at: typing.Optional[int] = None,
        layer: typing.Optional[int] = None,
        axis_sections: typing.Optional[typing.List[AxisSection]] = None,
        comment: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        time_type_id: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        body: typing.Optional[TimeEntriesUpdateMultipleRequest] = None,
        validate: bool = False,
        **kwargs,
    ) -> TimeEntriesUpdateMultipleResponsePydantic:
        raw_response = await self.raw.aupdate_multiple(
            body=body,
            id=id,
            starts_at=starts_at,
            duration=duration,
            unit=unit,
            ends_at=ends_at,
            owner_id=owner_id,
            author_id=author_id,
            created_at=created_at,
            creation_source=creation_source,
            modifier_id=modifier_id,
            modified_at=modified_at,
            layer=layer,
            axis_sections=axis_sections,
            comment=comment,
            time_type_id=time_type_id,
            **kwargs,
        )
        if validate:
            return TimeEntriesUpdateMultipleResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(TimeEntriesUpdateMultipleResponsePydantic, raw_response.body)
    
    
    @api_client.DeprecationWarningOnce(prefix="time_entries")
    def update_multiple(
        self,
        id: typing.Optional[int] = None,
        starts_at: typing.Optional[datetime] = None,
        duration: typing.Optional[str] = None,
        unit: typing.Optional[int] = None,
        ends_at: typing.Optional[datetime] = None,
        owner_id: typing.Optional[int] = None,
        author_id: typing.Optional[int] = None,
        created_at: typing.Optional[datetime] = None,
        creation_source: typing.Optional[int] = None,
        modifier_id: typing.Optional[int] = None,
        modified_at: typing.Optional[int] = None,
        layer: typing.Optional[int] = None,
        axis_sections: typing.Optional[typing.List[AxisSection]] = None,
        comment: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        time_type_id: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        body: typing.Optional[TimeEntriesUpdateMultipleRequest] = None,
        validate: bool = False,
    ) -> TimeEntriesUpdateMultipleResponsePydantic:
        raw_response = self.raw.update_multiple(
            body=body,
            id=id,
            starts_at=starts_at,
            duration=duration,
            unit=unit,
            ends_at=ends_at,
            owner_id=owner_id,
            author_id=author_id,
            created_at=created_at,
            creation_source=creation_source,
            modifier_id=modifier_id,
            modified_at=modified_at,
            layer=layer,
            axis_sections=axis_sections,
            comment=comment,
            time_type_id=time_type_id,
        )
        if validate:
            return TimeEntriesUpdateMultipleResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(TimeEntriesUpdateMultipleResponsePydantic, raw_response.body)


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @api_client.DeprecationWarningOnce(prefix="time_entries")
    async def aput(
        self,
        id: typing.Optional[int] = None,
        starts_at: typing.Optional[datetime] = None,
        duration: typing.Optional[str] = None,
        unit: typing.Optional[int] = None,
        ends_at: typing.Optional[datetime] = None,
        owner_id: typing.Optional[int] = None,
        author_id: typing.Optional[int] = None,
        created_at: typing.Optional[datetime] = None,
        creation_source: typing.Optional[int] = None,
        modifier_id: typing.Optional[int] = None,
        modified_at: typing.Optional[int] = None,
        layer: typing.Optional[int] = None,
        axis_sections: typing.Optional[typing.List[AxisSection]] = None,
        comment: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        time_type_id: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        body: typing.Optional[TimeEntriesUpdateMultipleRequest] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_multiple_mapped_args(
            body=body,
            id=id,
            starts_at=starts_at,
            duration=duration,
            unit=unit,
            ends_at=ends_at,
            owner_id=owner_id,
            author_id=author_id,
            created_at=created_at,
            creation_source=creation_source,
            modifier_id=modifier_id,
            modified_at=modified_at,
            layer=layer,
            axis_sections=axis_sections,
            comment=comment,
            time_type_id=time_type_id,
        )
        return await self._aupdate_multiple_oapg(
            body=args.body,
            **kwargs,
        )
    
    @api_client.DeprecationWarningOnce(prefix="time_entries")
    def put(
        self,
        id: typing.Optional[int] = None,
        starts_at: typing.Optional[datetime] = None,
        duration: typing.Optional[str] = None,
        unit: typing.Optional[int] = None,
        ends_at: typing.Optional[datetime] = None,
        owner_id: typing.Optional[int] = None,
        author_id: typing.Optional[int] = None,
        created_at: typing.Optional[datetime] = None,
        creation_source: typing.Optional[int] = None,
        modifier_id: typing.Optional[int] = None,
        modified_at: typing.Optional[int] = None,
        layer: typing.Optional[int] = None,
        axis_sections: typing.Optional[typing.List[AxisSection]] = None,
        comment: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        time_type_id: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        body: typing.Optional[TimeEntriesUpdateMultipleRequest] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_multiple_mapped_args(
            body=body,
            id=id,
            starts_at=starts_at,
            duration=duration,
            unit=unit,
            ends_at=ends_at,
            owner_id=owner_id,
            author_id=author_id,
            created_at=created_at,
            creation_source=creation_source,
            modifier_id=modifier_id,
            modified_at=modified_at,
            layer=layer,
            axis_sections=axis_sections,
            comment=comment,
            time_type_id=time_type_id,
        )
        return self._update_multiple_oapg(
            body=args.body,
        )

