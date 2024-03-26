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

from lucca_timmi_timesheet_python_sdk.model.workflow_deny_timesheet_by_id_request_timesheets import WorkflowDenyTimesheetByIdRequestTimesheets as WorkflowDenyTimesheetByIdRequestTimesheetsSchema
from lucca_timmi_timesheet_python_sdk.model.workflow_deny_timesheet_by_id_request import WorkflowDenyTimesheetByIdRequest as WorkflowDenyTimesheetByIdRequestSchema
from lucca_timmi_timesheet_python_sdk.model.workflow_send_reminder_email_response import WorkflowSendReminderEmailResponse as WorkflowSendReminderEmailResponseSchema

from lucca_timmi_timesheet_python_sdk.type.workflow_send_reminder_email_response import WorkflowSendReminderEmailResponse
from lucca_timmi_timesheet_python_sdk.type.workflow_deny_timesheet_by_id_request_timesheets import WorkflowDenyTimesheetByIdRequestTimesheets
from lucca_timmi_timesheet_python_sdk.type.workflow_deny_timesheet_by_id_request import WorkflowDenyTimesheetByIdRequest

from ...api_client import Dictionary
from lucca_timmi_timesheet_python_sdk.pydantic.workflow_send_reminder_email_response import WorkflowSendReminderEmailResponse as WorkflowSendReminderEmailResponsePydantic
from lucca_timmi_timesheet_python_sdk.pydantic.workflow_deny_timesheet_by_id_request_timesheets import WorkflowDenyTimesheetByIdRequestTimesheets as WorkflowDenyTimesheetByIdRequestTimesheetsPydantic
from lucca_timmi_timesheet_python_sdk.pydantic.workflow_deny_timesheet_by_id_request import WorkflowDenyTimesheetByIdRequest as WorkflowDenyTimesheetByIdRequestPydantic

# body param
SchemaForRequestBodyApplicationJson = WorkflowDenyTimesheetByIdRequestSchema


request_body_workflow_deny_timesheet_by_id_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor200ResponseBodyApplicationJson = WorkflowSendReminderEmailResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: WorkflowSendReminderEmailResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: WorkflowSendReminderEmailResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = WorkflowSendReminderEmailResponseSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: WorkflowSendReminderEmailResponse


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: WorkflowSendReminderEmailResponse


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor401ResponseBodyApplicationJson = WorkflowSendReminderEmailResponseSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: WorkflowSendReminderEmailResponse


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: WorkflowSendReminderEmailResponse


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)
SchemaFor403ResponseBodyApplicationJson = WorkflowSendReminderEmailResponseSchema


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: WorkflowSendReminderEmailResponse


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: WorkflowSendReminderEmailResponse


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationJson),
    },
)
SchemaFor404ResponseBodyApplicationJson = WorkflowSendReminderEmailResponseSchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: WorkflowSendReminderEmailResponse


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: WorkflowSendReminderEmailResponse


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
    },
)
SchemaFor500ResponseBodyApplicationJson = WorkflowSendReminderEmailResponseSchema


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: WorkflowSendReminderEmailResponse


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: WorkflowSendReminderEmailResponse


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    response_cls_async=ApiResponseFor500Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _deny_timesheet_by_id_mapped_args(
        self,
        timesheets: typing.Optional[WorkflowDenyTimesheetByIdRequestTimesheets] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if timesheets is not None:
            _body["timesheets"] = timesheets
        args.body = _body
        return args

    async def _adeny_timesheet_by_id_oapg(
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
        Deny Timesheets by id
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
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/timmi/services/workflow/deny',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_workflow_deny_timesheet_by_id_request.serialize(body, content_type)
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


    def _deny_timesheet_by_id_oapg(
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
        Deny Timesheets by id
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
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/timmi/services/workflow/deny',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_workflow_deny_timesheet_by_id_request.serialize(body, content_type)
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


class DenyTimesheetByIdRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def adeny_timesheet_by_id(
        self,
        timesheets: typing.Optional[WorkflowDenyTimesheetByIdRequestTimesheets] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._deny_timesheet_by_id_mapped_args(
            timesheets=timesheets,
        )
        return await self._adeny_timesheet_by_id_oapg(
            body=args.body,
            **kwargs,
        )
    
    def deny_timesheet_by_id(
        self,
        timesheets: typing.Optional[WorkflowDenyTimesheetByIdRequestTimesheets] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._deny_timesheet_by_id_mapped_args(
            timesheets=timesheets,
        )
        return self._deny_timesheet_by_id_oapg(
            body=args.body,
        )

class DenyTimesheetById(BaseApi):

    async def adeny_timesheet_by_id(
        self,
        timesheets: typing.Optional[WorkflowDenyTimesheetByIdRequestTimesheets] = None,
        validate: bool = False,
        **kwargs,
    ) -> WorkflowSendReminderEmailResponsePydantic:
        raw_response = await self.raw.adeny_timesheet_by_id(
            timesheets=timesheets,
            **kwargs,
        )
        if validate:
            return WorkflowSendReminderEmailResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(WorkflowSendReminderEmailResponsePydantic, raw_response.body)
    
    
    def deny_timesheet_by_id(
        self,
        timesheets: typing.Optional[WorkflowDenyTimesheetByIdRequestTimesheets] = None,
        validate: bool = False,
    ) -> WorkflowSendReminderEmailResponsePydantic:
        raw_response = self.raw.deny_timesheet_by_id(
            timesheets=timesheets,
        )
        if validate:
            return WorkflowSendReminderEmailResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(WorkflowSendReminderEmailResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        timesheets: typing.Optional[WorkflowDenyTimesheetByIdRequestTimesheets] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._deny_timesheet_by_id_mapped_args(
            timesheets=timesheets,
        )
        return await self._adeny_timesheet_by_id_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        timesheets: typing.Optional[WorkflowDenyTimesheetByIdRequestTimesheets] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._deny_timesheet_by_id_mapped_args(
            timesheets=timesheets,
        )
        return self._deny_timesheet_by_id_oapg(
            body=args.body,
        )

