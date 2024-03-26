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

from lucca_timmi_timesheet_python_sdk.pydantic.report_columns import ReportColumns

class Report(BaseModel):
    template_id: str = Field(alias='templateId')

    id: typing.Optional[int] = Field(None, alias='id')

    status: typing.Optional[Literal["pending", "done", "error"]] = Field(None, alias='status')

    name: typing.Optional[str] = Field(None, alias='name')

    starts_on: typing.Optional[date] = Field(None, alias='startsOn')

    ends_on: typing.Optional[date] = Field(None, alias='endsOn')

    filters: typing.Optional[typing.List[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = Field(None, alias='filters')

    columns: typing.Optional[ReportColumns] = Field(None, alias='columns')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
