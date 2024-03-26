# coding: utf-8

"""
    Timmi Timesheet API

    Welcome on the documentation for the Timmi Timesheet API. 

    The version of the OpenAPI document: 1.0
    Contact: developers@lucca.fr
    Created by: https://www.lucca.fr
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from lucca_timmi_timesheet_python_sdk.type.timesheets_list_due_response_data import TimesheetsListDueResponseData

class RequiredTimesheetsListDueResponse(TypedDict):
    pass

class OptionalTimesheetsListDueResponse(TypedDict, total=False):
    data: TimesheetsListDueResponseData

class TimesheetsListDueResponse(RequiredTimesheetsListDueResponse, OptionalTimesheetsListDueResponse):
    pass
