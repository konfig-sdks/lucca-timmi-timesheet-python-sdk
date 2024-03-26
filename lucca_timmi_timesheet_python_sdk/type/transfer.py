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


class RequiredTransfer(TypedDict):
    pass

class OptionalTransfer(TypedDict, total=False):
    # Unique identifier of the associated transfer authorization.
    transferAuthorizationId: int

    # Format: d.hh:mm:ss. Max: \"1.00:00:00\" (ie 24 hours).
    amount: str

    comment: str

class Transfer(RequiredTransfer, OptionalTransfer):
    pass
