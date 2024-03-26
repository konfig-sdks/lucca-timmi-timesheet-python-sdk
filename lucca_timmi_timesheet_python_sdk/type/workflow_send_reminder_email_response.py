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

from lucca_timmi_timesheet_python_sdk.type.workflow_send_reminder_email_response_items import WorkflowSendReminderEmailResponseItems

class RequiredWorkflowSendReminderEmailResponse(TypedDict):
    pass

class OptionalWorkflowSendReminderEmailResponse(TypedDict, total=False):
    # HTTP status code.
    Status: int

    # Human readable error message (when error).
    Message: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    Items: WorkflowSendReminderEmailResponseItems

class WorkflowSendReminderEmailResponse(RequiredWorkflowSendReminderEmailResponse, OptionalWorkflowSendReminderEmailResponse):
    pass
