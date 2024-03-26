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

from lucca_timmi_timesheet_python_sdk.type.time_entry import TimeEntry

class RequiredTimeEntriesCreateMultipleResponse(TypedDict):
    pass

class OptionalTimeEntriesCreateMultipleResponse(TypedDict, total=False):
    data: typing.Union[TimeEntry, typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]

class TimeEntriesCreateMultipleResponse(RequiredTimeEntriesCreateMultipleResponse, OptionalTimeEntriesCreateMultipleResponse):
    pass
