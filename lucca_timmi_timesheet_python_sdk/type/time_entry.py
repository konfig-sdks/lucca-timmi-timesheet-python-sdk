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

from lucca_timmi_timesheet_python_sdk.type.axis_section import AxisSection

class RequiredTimeEntry(TypedDict):
    # The timeEntry start date and time. Please do NOT send any offset/timezone information (\"Z\", \"+01:00\", etc...).
    startsAt: datetime

    # Format: d.hh:mm:ss. Max: \"1.00:00:00\" (ie 24 hours).
    duration: str

    # 0: Days (eg \"1/2 day\"). 1: Hours (eg \"8h15min\"). 2: Time (eg \"23:45:00\").
    unit: int

    # The user's unique identifier.
    ownerId: int

class OptionalTimeEntry(TypedDict, total=False):
    # Unique identifier for this object.
    id: int

    endsAt: datetime

    # Identifier of the user who initially created this TimeEntry.
    authorId: int

    createdAt: datetime

    # 0: Fallback on theoretical TimeEntries. 1: Application of bookmarked week. 2: Manual creation. 3: Import
    creationSource: int

    # The unique identifier of the user who last updated the TimeEntry.
    modifierId: int

    # Date and time when TimeEntry was last modified.
    modifiedAt: int

    # 0: Actual. 1: Theoretical
    layer: int

    # When not in activity mode, send an empty array, or do not serialize this property.
    axisSections: typing.List[AxisSection]

    # Only used on activities (TimeEntries w/ AxisSections).
    comment: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    timeTypeId: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class TimeEntry(RequiredTimeEntry, OptionalTimeEntry):
    pass
