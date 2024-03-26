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


class TimesheetUser(BaseModel):
    # Unique identifier of this User.
    id: typing.Optional[int] = Field(None, alias='id')

    # Given name.
    first_name: typing.Optional[str] = Field(None, alias='firstName')

    # Family name
    last_name: typing.Optional[str] = Field(None, alias='lastName')

    # Email address.
    mail: typing.Optional[str] = Field(None, alias='mail')

    # Unique identifier of the legal establishment this user currently has a work contract with.
    legal_entity_id: typing.Optional[int] = Field(None, alias='legalEntityId')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
