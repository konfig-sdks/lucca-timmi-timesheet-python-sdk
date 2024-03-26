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


class RequiredTimesheetUser(TypedDict):
    pass

class OptionalTimesheetUser(TypedDict, total=False):
    # Unique identifier of this User.
    id: int

    # Given name.
    firstName: str

    # Family name
    lastName: str

    # Email address.
    mail: str

    # Unique identifier of the legal establishment this user currently has a work contract with.
    legalEntityId: int

class TimesheetUser(RequiredTimesheetUser, OptionalTimesheetUser):
    pass
