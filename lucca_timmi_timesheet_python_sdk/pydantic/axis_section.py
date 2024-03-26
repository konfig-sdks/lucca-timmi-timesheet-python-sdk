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


class AxisSection(BaseModel):
    description: typing.Optional[str] = Field(None, alias='description')

    id: typing.Optional[int] = Field(None, alias='id')

    code: typing.Optional[str] = Field(None, alias='code')

    name: typing.Optional[str] = Field(None, alias='name')

    multilingual_name: typing.Optional[str] = Field(None, alias='multilingualName')

    owner_id: typing.Optional[int] = Field(None, alias='ownerId')

    start_on: typing.Optional[datetime] = Field(None, alias='startOn')

    end_on: typing.Optional[datetime] = Field(None, alias='endOn')

    active: typing.Optional[bool] = Field(None, alias='active')

    axis_id: typing.Optional[int] = Field(None, alias='axisId')

    parent_axis_sections: typing.Optional['typing.List["AxisSection"]'] = Field(None, alias='parentAxisSections')

    children_axis_sections: typing.Optional['typing.List["AxisSection"]'] = Field(None, alias='childrenAxisSections')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
