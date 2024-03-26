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


class RequiredReportColumnsItem(TypedDict):
    pass

class OptionalReportColumnsItem(TypedDict, total=False):
    kind: str

    name: str

    category: str

    isRequired: bool

    isDefault: bool

    # Periodic columns will be duplicated as many times as there are occurrences of periodicity in the report.
    isPeriodic: bool

class ReportColumnsItem(RequiredReportColumnsItem, OptionalReportColumnsItem):
    pass
