# coding: utf-8

"""
    Timmi Timesheet API

    Welcome on the documentation for the Timmi Timesheet API. 

    The version of the OpenAPI document: 1.0
    Contact: developers@lucca.fr
    Created by: https://www.lucca.fr
"""

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


class WorkflowDenyTimesheetByIdRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def timesheets() -> typing.Type['WorkflowDenyTimesheetByIdRequestTimesheets']:
                return WorkflowDenyTimesheetByIdRequestTimesheets
            __annotations__ = {
                "timesheets": timesheets,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timesheets"]) -> 'WorkflowDenyTimesheetByIdRequestTimesheets': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["timesheets", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timesheets"]) -> typing.Union['WorkflowDenyTimesheetByIdRequestTimesheets', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["timesheets", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        timesheets: typing.Union['WorkflowDenyTimesheetByIdRequestTimesheets', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WorkflowDenyTimesheetByIdRequest':
        return super().__new__(
            cls,
            *args,
            timesheets=timesheets,
            _configuration=_configuration,
            **kwargs,
        )

from lucca_timmi_timesheet_python_sdk.model.workflow_deny_timesheet_by_id_request_timesheets import WorkflowDenyTimesheetByIdRequestTimesheets
