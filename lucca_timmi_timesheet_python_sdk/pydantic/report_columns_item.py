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


class ReportColumnsItem(BaseModel):
    kind: typing.Optional[str] = Field(None, alias='kind')

    name: typing.Optional[str] = Field(None, alias='name')

    category: typing.Optional[str] = Field(None, alias='category')

    is_required: typing.Optional[bool] = Field(None, alias='isRequired')

    is_default: typing.Optional[bool] = Field(None, alias='isDefault')

    # Periodic columns will be duplicated as many times as there are occurrences of periodicity in the report.
    is_periodic: typing.Optional[bool] = Field(None, alias='isPeriodic')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
