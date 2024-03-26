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

from lucca_timmi_timesheet_python_sdk.pydantic.axis_section import AxisSection

class TimeEntry(BaseModel):
    # The timeEntry start date and time. Please do NOT send any offset/timezone information (\"Z\", \"+01:00\", etc...).
    starts_at: datetime = Field(alias='startsAt')

    # Format: d.hh:mm:ss. Max: \"1.00:00:00\" (ie 24 hours).
    duration: str = Field(alias='duration')

    # 0: Days (eg \"1/2 day\"). 1: Hours (eg \"8h15min\"). 2: Time (eg \"23:45:00\").
    unit: Literal[0, 1, 2] = Field(alias='unit')

    # The user's unique identifier.
    owner_id: int = Field(alias='ownerId')

    # Unique identifier for this object.
    id: typing.Optional[int] = Field(None, alias='id')

    ends_at: typing.Optional[datetime] = Field(None, alias='endsAt')

    # Identifier of the user who initially created this TimeEntry.
    author_id: typing.Optional[int] = Field(None, alias='authorId')

    created_at: typing.Optional[datetime] = Field(None, alias='createdAt')

    # 0: Fallback on theoretical TimeEntries. 1: Application of bookmarked week. 2: Manual creation. 3: Import
    creation_source: typing.Optional[Literal[0, 1, 2, 3]] = Field(None, alias='creationSource')

    # The unique identifier of the user who last updated the TimeEntry.
    modifier_id: typing.Optional[int] = Field(None, alias='modifierId')

    # Date and time when TimeEntry was last modified.
    modified_at: typing.Optional[int] = Field(None, alias='modifiedAt')

    # 0: Actual. 1: Theoretical
    layer: typing.Optional[int] = Field(None, alias='layer')

    # When not in activity mode, send an empty array, or do not serialize this property.
    axis_sections: typing.Optional[typing.List[AxisSection]] = Field(None, alias='axisSections')

    # Only used on activities (TimeEntries w/ AxisSections).
    comment: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='comment')

    time_type_id: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='timeTypeId')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
