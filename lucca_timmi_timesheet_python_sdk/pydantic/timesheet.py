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

from lucca_timmi_timesheet_python_sdk.pydantic.timesheet_user import TimesheetUser

class Timesheet(BaseModel):
    id: typing.Optional[str] = Field(None, alias='id')

    # - 0: the timesheet is yet to be submitted - 1: the timesheet has been submitted and approval is still pending - 2: the timesheet has been submitted and approved. - 3: the timesheet has been rejected (cancelled after submission, denied upon approval or invalidated after having been approved) 
    status: typing.Optional[Literal[0, 1, 2, 3]] = Field(None, alias='status')

    starts_on: typing.Optional[date] = Field(None, alias='startsOn')

    ends_on: typing.Optional[str] = Field(None, alias='endsOn')

    owner_id: typing.Optional[int] = Field(None, alias='ownerId')

    owner: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='owner')

    # Identifier of the applicable \"statute\" (configuration).
    statute_id: typing.Optional[int] = Field(None, alias='statuteId')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
