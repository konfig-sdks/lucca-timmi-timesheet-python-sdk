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

from lucca_timmi_timesheet_python_sdk.model.time_entries_list_time_entries_response import TimeEntriesListTimeEntriesResponse as TimeEntriesListTimeEntriesResponseSchema
from lucca_timmi_timesheet_python_sdk.model.time_entries_delete_multiple_response import TimeEntriesDeleteMultipleResponse as TimeEntriesDeleteMultipleResponseSchema

from lucca_timmi_timesheet_python_sdk.type.time_entries_delete_multiple_response import TimeEntriesDeleteMultipleResponse
from lucca_timmi_timesheet_python_sdk.type.time_entries_list_time_entries_response import TimeEntriesListTimeEntriesResponse

from ...api_client import Dictionary
from lucca_timmi_timesheet_python_sdk.pydantic.time_entries_list_time_entries_response import TimeEntriesListTimeEntriesResponse as TimeEntriesListTimeEntriesResponsePydantic
from lucca_timmi_timesheet_python_sdk.pydantic.time_entries_delete_multiple_response import TimeEntriesDeleteMultipleResponse as TimeEntriesDeleteMultipleResponsePydantic

from . import path

# Query params
PagingSchema = schemas.StrSchema


class OwnerIdSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.AnyTypeSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'OwnerIdSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
StartsAtSchema = schemas.StrSchema


class AxisSectionsIdSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.AnyTypeSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'AxisSectionsIdSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)


class AxisSectionsCodeSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.AnyTypeSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'AxisSectionsCodeSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
ModifiedAtSchema = schemas.StrSchema
ArchivedAtSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'paging': typing.Union[PagingSchema, str, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'ownerId': typing.Union[OwnerIdSchema, list, tuple, ],
        'startsAt': typing.Union[StartsAtSchema, str, ],
        'axisSections.id': typing.Union[AxisSectionsIdSchema, list, tuple, ],
        'axisSections.code': typing.Union[AxisSectionsCodeSchema, list, tuple, ],
        'modifiedAt': typing.Union[ModifiedAtSchema, str, ],
        'archivedAt': typing.Union[ArchivedAtSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_paging = api_client.QueryParameter(
    name="paging",
    style=api_client.ParameterStyle.FORM,
    schema=PagingSchema,
    required=True,
    explode=True,
)
request_query_owner_id = api_client.QueryParameter(
    name="ownerId",
    style=api_client.ParameterStyle.FORM,
    schema=OwnerIdSchema,
    explode=True,
)
request_query_starts_at = api_client.QueryParameter(
    name="startsAt",
    style=api_client.ParameterStyle.FORM,
    schema=StartsAtSchema,
    explode=True,
)
request_query_axis_sections_id = api_client.QueryParameter(
    name="axisSections.id",
    style=api_client.ParameterStyle.FORM,
    schema=AxisSectionsIdSchema,
    explode=True,
)
request_query_axis_sections_code = api_client.QueryParameter(
    name="axisSections.code",
    style=api_client.ParameterStyle.FORM,
    schema=AxisSectionsCodeSchema,
    explode=True,
)
request_query_modified_at = api_client.QueryParameter(
    name="modifiedAt",
    style=api_client.ParameterStyle.FORM,
    schema=ModifiedAtSchema,
    explode=True,
)
request_query_archived_at = api_client.QueryParameter(
    name="archivedAt",
    style=api_client.ParameterStyle.FORM,
    schema=ArchivedAtSchema,
    explode=True,
)
_auth = [
    'Authorization',
]
SchemaFor200ResponseBodyApplicationJson = TimeEntriesListTimeEntriesResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: TimeEntriesListTimeEntriesResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: TimeEntriesListTimeEntriesResponse


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
SchemaFor404ResponseBodyApplicationJson = TimeEntriesDeleteMultipleResponseSchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: TimeEntriesDeleteMultipleResponse


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: TimeEntriesDeleteMultipleResponse


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
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
    '404': _response_for_404,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _list_time_entries_mapped_args(
        self,
        paging: str,
        owner_id: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        starts_at: typing.Optional[str] = None,
        axis_sections_id: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        axis_sections_code: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        modified_at: typing.Optional[str] = None,
        archived_at: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if paging is not None:
            _query_params["paging"] = paging
        if owner_id is not None:
            _query_params["ownerId"] = owner_id
        if starts_at is not None:
            _query_params["startsAt"] = starts_at
        if axis_sections_id is not None:
            _query_params["axisSections.id"] = axis_sections_id
        if axis_sections_code is not None:
            _query_params["axisSections.code"] = axis_sections_code
        if modified_at is not None:
            _query_params["modifiedAt"] = modified_at
        if archived_at is not None:
            _query_params["archivedAt"] = archived_at
        args.query = _query_params
        return args

    async def _alist_time_entries_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        List TimeEntries
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_paging,
            request_query_owner_id,
            request_query_starts_at,
            request_query_axis_sections_id,
            request_query_axis_sections_code,
            request_query_modified_at,
            request_query_archived_at,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v3/timeentries',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
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


    def _list_time_entries_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        List TimeEntries
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_paging,
            request_query_owner_id,
            request_query_starts_at,
            request_query_axis_sections_id,
            request_query_axis_sections_code,
            request_query_modified_at,
            request_query_archived_at,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v3/timeentries',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
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


class ListTimeEntriesRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def alist_time_entries(
        self,
        paging: str,
        owner_id: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        starts_at: typing.Optional[str] = None,
        axis_sections_id: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        axis_sections_code: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        modified_at: typing.Optional[str] = None,
        archived_at: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_time_entries_mapped_args(
            paging=paging,
            owner_id=owner_id,
            starts_at=starts_at,
            axis_sections_id=axis_sections_id,
            axis_sections_code=axis_sections_code,
            modified_at=modified_at,
            archived_at=archived_at,
        )
        return await self._alist_time_entries_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def list_time_entries(
        self,
        paging: str,
        owner_id: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        starts_at: typing.Optional[str] = None,
        axis_sections_id: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        axis_sections_code: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        modified_at: typing.Optional[str] = None,
        archived_at: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_time_entries_mapped_args(
            paging=paging,
            owner_id=owner_id,
            starts_at=starts_at,
            axis_sections_id=axis_sections_id,
            axis_sections_code=axis_sections_code,
            modified_at=modified_at,
            archived_at=archived_at,
        )
        return self._list_time_entries_oapg(
            query_params=args.query,
        )

class ListTimeEntries(BaseApi):

    async def alist_time_entries(
        self,
        paging: str,
        owner_id: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        starts_at: typing.Optional[str] = None,
        axis_sections_id: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        axis_sections_code: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        modified_at: typing.Optional[str] = None,
        archived_at: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> TimeEntriesListTimeEntriesResponsePydantic:
        raw_response = await self.raw.alist_time_entries(
            paging=paging,
            owner_id=owner_id,
            starts_at=starts_at,
            axis_sections_id=axis_sections_id,
            axis_sections_code=axis_sections_code,
            modified_at=modified_at,
            archived_at=archived_at,
            **kwargs,
        )
        if validate:
            return TimeEntriesListTimeEntriesResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(TimeEntriesListTimeEntriesResponsePydantic, raw_response.body)
    
    
    def list_time_entries(
        self,
        paging: str,
        owner_id: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        starts_at: typing.Optional[str] = None,
        axis_sections_id: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        axis_sections_code: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        modified_at: typing.Optional[str] = None,
        archived_at: typing.Optional[str] = None,
        validate: bool = False,
    ) -> TimeEntriesListTimeEntriesResponsePydantic:
        raw_response = self.raw.list_time_entries(
            paging=paging,
            owner_id=owner_id,
            starts_at=starts_at,
            axis_sections_id=axis_sections_id,
            axis_sections_code=axis_sections_code,
            modified_at=modified_at,
            archived_at=archived_at,
        )
        if validate:
            return TimeEntriesListTimeEntriesResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(TimeEntriesListTimeEntriesResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        paging: str,
        owner_id: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        starts_at: typing.Optional[str] = None,
        axis_sections_id: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        axis_sections_code: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        modified_at: typing.Optional[str] = None,
        archived_at: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_time_entries_mapped_args(
            paging=paging,
            owner_id=owner_id,
            starts_at=starts_at,
            axis_sections_id=axis_sections_id,
            axis_sections_code=axis_sections_code,
            modified_at=modified_at,
            archived_at=archived_at,
        )
        return await self._alist_time_entries_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        paging: str,
        owner_id: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        starts_at: typing.Optional[str] = None,
        axis_sections_id: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        axis_sections_code: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        modified_at: typing.Optional[str] = None,
        archived_at: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_time_entries_mapped_args(
            paging=paging,
            owner_id=owner_id,
            starts_at=starts_at,
            axis_sections_id=axis_sections_id,
            axis_sections_code=axis_sections_code,
            modified_at=modified_at,
            archived_at=archived_at,
        )
        return self._list_time_entries_oapg(
            query_params=args.query,
        )

