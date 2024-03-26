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


class WorkflowInvalidateTimesheetByIdRequestTimesheets(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['WorkflowInvalidateTimesheetByIdRequestTimesheetsItem']:
            return WorkflowInvalidateTimesheetByIdRequestTimesheetsItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['WorkflowInvalidateTimesheetByIdRequestTimesheetsItem'], typing.List['WorkflowInvalidateTimesheetByIdRequestTimesheetsItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'WorkflowInvalidateTimesheetByIdRequestTimesheets':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'WorkflowInvalidateTimesheetByIdRequestTimesheetsItem':
        return super().__getitem__(i)

from lucca_timmi_timesheet_python_sdk.model.workflow_invalidate_timesheet_by_id_request_timesheets_item import WorkflowInvalidateTimesheetByIdRequestTimesheetsItem
