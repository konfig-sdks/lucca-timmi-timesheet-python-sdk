# coding: utf-8

"""
    Timmi Timesheet API

    Welcome on the documentation for the Timmi Timesheet API. 

    The version of the OpenAPI document: 1.0
    Contact: developers@lucca.fr
    Created by: https://www.lucca.fr
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from lucca_timmi_timesheet_python_sdk import schemas  # noqa: F401


class WorkflowSendReminderEmailResponseItems(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['WorkflowSendReminderEmailResponseItemsItem']:
            return WorkflowSendReminderEmailResponseItemsItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['WorkflowSendReminderEmailResponseItemsItem'], typing.List['WorkflowSendReminderEmailResponseItemsItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'WorkflowSendReminderEmailResponseItems':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'WorkflowSendReminderEmailResponseItemsItem':
        return super().__getitem__(i)

from lucca_timmi_timesheet_python_sdk.model.workflow_send_reminder_email_response_items_item import WorkflowSendReminderEmailResponseItemsItem
