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

from lucca_timmi_timesheet_python_sdk.pydantic.workflow_send_reminder_email_response_items import WorkflowSendReminderEmailResponseItems

class WorkflowSendReminderEmailResponse(BaseModel):
    # HTTP status code.
    status: typing.Optional[int] = Field(None, alias='Status')

    # Human readable error message (when error).
    message: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='Message')

    items: typing.Optional[WorkflowSendReminderEmailResponseItems] = Field(None, alias='Items')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
