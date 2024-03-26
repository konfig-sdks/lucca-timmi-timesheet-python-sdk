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


class RequiredAxisSection(TypedDict):
    pass

class OptionalAxisSection(TypedDict, total=False):
    description: str

    id: int

    code: str

    name: str

    multilingualName: str

    ownerId: int

    startOn: datetime

    endOn: datetime

    active: bool

    axisId: int

    parentAxisSections: 'typing.List["AxisSection"]'

    childrenAxisSections: 'typing.List["AxisSection"]'

class AxisSection(RequiredAxisSection, OptionalAxisSection):
    pass
