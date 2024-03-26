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

from lucca_timmi_timesheet_python_sdk.type.workflow_invalidate_timesheet_by_id_request_timesheets import WorkflowInvalidateTimesheetByIdRequestTimesheets

class RequiredWorkflowInvalidateTimesheetByIdRequest(TypedDict):
    pass

class OptionalWorkflowInvalidateTimesheetByIdRequest(TypedDict, total=False):
    timesheets: WorkflowInvalidateTimesheetByIdRequestTimesheets

class WorkflowInvalidateTimesheetByIdRequest(RequiredWorkflowInvalidateTimesheetByIdRequest, OptionalWorkflowInvalidateTimesheetByIdRequest):
    pass
