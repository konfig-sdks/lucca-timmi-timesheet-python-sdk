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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from lucca_timmi_timesheet_python_sdk.pydantic.time_entry import TimeEntry

class TimeEntriesUpdateMultipleResponse(BaseModel):
    data: typing.Optional[typing.Union[TimeEntry, typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = Field(None, alias='data')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
