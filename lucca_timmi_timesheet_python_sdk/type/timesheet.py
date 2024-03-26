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

from lucca_timmi_timesheet_python_sdk.type.timesheet_user import TimesheetUser

class RequiredTimesheet(TypedDict):
    pass

class OptionalTimesheet(TypedDict, total=False):
    id: str

    # - 0: the timesheet is yet to be submitted - 1: the timesheet has been submitted and approval is still pending - 2: the timesheet has been submitted and approved. - 3: the timesheet has been rejected (cancelled after submission, denied upon approval or invalidated after having been approved) 
    status: int

    startsOn: date

    endsOn: str

    ownerId: int

    owner: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # Identifier of the applicable \"statute\" (configuration).
    statuteId: int

class Timesheet(RequiredTimesheet, OptionalTimesheet):
    pass
