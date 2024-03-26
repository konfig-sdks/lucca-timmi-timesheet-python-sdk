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

from lucca_timmi_timesheet_python_sdk.pydantic.workflow_approve_timesheets_by_id_request_timesheets import WorkflowApproveTimesheetsByIdRequestTimesheets

class WorkflowApproveTimesheetsByIdRequest(BaseModel):
    timesheets: typing.Optional[WorkflowApproveTimesheetsByIdRequestTimesheets] = Field(None, alias='timesheets')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
