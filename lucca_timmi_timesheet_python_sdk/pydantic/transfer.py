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


class Transfer(BaseModel):
    # Unique identifier of the associated transfer authorization.
    transfer_authorization_id: typing.Optional[int] = Field(None, alias='transferAuthorizationId')

    # Format: d.hh:mm:ss. Max: \"1.00:00:00\" (ie 24 hours).
    amount: typing.Optional[str] = Field(None, alias='amount')

    comment: typing.Optional[str] = Field(None, alias='comment')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
