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


class RequiredWorkflowCancelTimesheetByIdRequestTimesheetsItem(TypedDict):
    id: int

class OptionalWorkflowCancelTimesheetByIdRequestTimesheetsItem(TypedDict, total=False):
    comment: str

class WorkflowCancelTimesheetByIdRequestTimesheetsItem(RequiredWorkflowCancelTimesheetByIdRequestTimesheetsItem, OptionalWorkflowCancelTimesheetByIdRequestTimesheetsItem):
    pass
