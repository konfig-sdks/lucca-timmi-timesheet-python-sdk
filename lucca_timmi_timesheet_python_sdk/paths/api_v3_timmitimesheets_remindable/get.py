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

from lucca_timmi_timesheet_python_sdk.model.time_entries_delete_multiple_response import TimeEntriesDeleteMultipleResponse as TimeEntriesDeleteMultipleResponseSchema
from lucca_timmi_timesheet_python_sdk.model.timesheets_list_due_response import TimesheetsListDueResponse as TimesheetsListDueResponseSchema

from lucca_timmi_timesheet_python_sdk.type.time_entries_delete_multiple_response import TimeEntriesDeleteMultipleResponse
from lucca_timmi_timesheet_python_sdk.type.timesheets_list_due_response import TimesheetsListDueResponse

from ...api_client import Dictionary
from lucca_timmi_timesheet_python_sdk.pydantic.timesheets_list_due_response import TimesheetsListDueResponse as TimesheetsListDueResponsePydantic
from lucca_timmi_timesheet_python_sdk.pydantic.time_entries_delete_multiple_response import TimeEntriesDeleteMultipleResponse as TimeEntriesDeleteMultipleResponsePydantic

from . import path

# Query params


class OwnerIdsSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.IntSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'OwnerIdsSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)


class LegalEntityIdsSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.IntSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'LegalEntityIdsSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)


class ManagerIdsSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.IntSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ManagerIdsSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
StartSchema = schemas.DateSchema
EndSchema = schemas.DateSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'ownerIds': typing.Union[OwnerIdsSchema, list, tuple, ],
        'legalEntityIds': typing.Union[LegalEntityIdsSchema, list, tuple, ],
        'managerIds': typing.Union[ManagerIdsSchema, list, tuple, ],
        'start': typing.Union[StartSchema, str, date, ],
        'end': typing.Union[EndSchema, str, date, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_owner_ids = api_client.QueryParameter(
    name="ownerIds",
    style=api_client.ParameterStyle.FORM,
    schema=OwnerIdsSchema,
    explode=True,
)
request_query_legal_entity_ids = api_client.QueryParameter(
    name="legalEntityIds",
    style=api_client.ParameterStyle.FORM,
    schema=LegalEntityIdsSchema,
    explode=True,
)
request_query_manager_ids = api_client.QueryParameter(
    name="managerIds",
    style=api_client.ParameterStyle.FORM,
    schema=ManagerIdsSchema,
    explode=True,
)
request_query_start = api_client.QueryParameter(
    name="start",
    style=api_client.ParameterStyle.FORM,
    schema=StartSchema,
    explode=True,
)
request_query_end = api_client.QueryParameter(
    name="end",
    style=api_client.ParameterStyle.FORM,
    schema=EndSchema,
    explode=True,
)
_auth = [
    'Authorization',
]
SchemaFor200ResponseBodyApplicationJson = TimesheetsListDueResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: TimesheetsListDueResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: TimesheetsListDueResponse


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
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _list_due_mapped_args(
        self,
        owner_ids: typing.Optional[typing.List[int]] = None,
        legal_entity_ids: typing.Optional[typing.List[int]] = None,
        manager_ids: typing.Optional[typing.List[int]] = None,
        start: typing.Optional[date] = None,
        end: typing.Optional[date] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if owner_ids is not None:
            _query_params["ownerIds"] = owner_ids
        if legal_entity_ids is not None:
            _query_params["legalEntityIds"] = legal_entity_ids
        if manager_ids is not None:
            _query_params["managerIds"] = manager_ids
        if start is not None:
            _query_params["start"] = start
        if end is not None:
            _query_params["end"] = end
        args.query = _query_params
        return args

    async def _alist_due_oapg(
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
        List due timesheets
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_owner_ids,
            request_query_legal_entity_ids,
            request_query_manager_ids,
            request_query_start,
            request_query_end,
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
            path_template='/api/v3/timmitimesheets/remindable',
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


    def _list_due_oapg(
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
        List due timesheets
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_owner_ids,
            request_query_legal_entity_ids,
            request_query_manager_ids,
            request_query_start,
            request_query_end,
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
            path_template='/api/v3/timmitimesheets/remindable',
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


class ListDueRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def alist_due(
        self,
        owner_ids: typing.Optional[typing.List[int]] = None,
        legal_entity_ids: typing.Optional[typing.List[int]] = None,
        manager_ids: typing.Optional[typing.List[int]] = None,
        start: typing.Optional[date] = None,
        end: typing.Optional[date] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_due_mapped_args(
            owner_ids=owner_ids,
            legal_entity_ids=legal_entity_ids,
            manager_ids=manager_ids,
            start=start,
            end=end,
        )
        return await self._alist_due_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def list_due(
        self,
        owner_ids: typing.Optional[typing.List[int]] = None,
        legal_entity_ids: typing.Optional[typing.List[int]] = None,
        manager_ids: typing.Optional[typing.List[int]] = None,
        start: typing.Optional[date] = None,
        end: typing.Optional[date] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_due_mapped_args(
            owner_ids=owner_ids,
            legal_entity_ids=legal_entity_ids,
            manager_ids=manager_ids,
            start=start,
            end=end,
        )
        return self._list_due_oapg(
            query_params=args.query,
        )

class ListDue(BaseApi):

    async def alist_due(
        self,
        owner_ids: typing.Optional[typing.List[int]] = None,
        legal_entity_ids: typing.Optional[typing.List[int]] = None,
        manager_ids: typing.Optional[typing.List[int]] = None,
        start: typing.Optional[date] = None,
        end: typing.Optional[date] = None,
        validate: bool = False,
        **kwargs,
    ) -> TimesheetsListDueResponsePydantic:
        raw_response = await self.raw.alist_due(
            owner_ids=owner_ids,
            legal_entity_ids=legal_entity_ids,
            manager_ids=manager_ids,
            start=start,
            end=end,
            **kwargs,
        )
        if validate:
            return TimesheetsListDueResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(TimesheetsListDueResponsePydantic, raw_response.body)
    
    
    def list_due(
        self,
        owner_ids: typing.Optional[typing.List[int]] = None,
        legal_entity_ids: typing.Optional[typing.List[int]] = None,
        manager_ids: typing.Optional[typing.List[int]] = None,
        start: typing.Optional[date] = None,
        end: typing.Optional[date] = None,
        validate: bool = False,
    ) -> TimesheetsListDueResponsePydantic:
        raw_response = self.raw.list_due(
            owner_ids=owner_ids,
            legal_entity_ids=legal_entity_ids,
            manager_ids=manager_ids,
            start=start,
            end=end,
        )
        if validate:
            return TimesheetsListDueResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(TimesheetsListDueResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        owner_ids: typing.Optional[typing.List[int]] = None,
        legal_entity_ids: typing.Optional[typing.List[int]] = None,
        manager_ids: typing.Optional[typing.List[int]] = None,
        start: typing.Optional[date] = None,
        end: typing.Optional[date] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_due_mapped_args(
            owner_ids=owner_ids,
            legal_entity_ids=legal_entity_ids,
            manager_ids=manager_ids,
            start=start,
            end=end,
        )
        return await self._alist_due_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        owner_ids: typing.Optional[typing.List[int]] = None,
        legal_entity_ids: typing.Optional[typing.List[int]] = None,
        manager_ids: typing.Optional[typing.List[int]] = None,
        start: typing.Optional[date] = None,
        end: typing.Optional[date] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_due_mapped_args(
            owner_ids=owner_ids,
            legal_entity_ids=legal_entity_ids,
            manager_ids=manager_ids,
            start=start,
            end=end,
        )
        return self._list_due_oapg(
            query_params=args.query,
        )

