# coding: utf-8
"""
    Timmi Timesheet API

    Welcome on the documentation for the Timmi Timesheet API. 

    The version of the OpenAPI document: 1.0
    Contact: developers@lucca.fr
    Created by: https://www.lucca.fr
"""

import typing
import inspect
from datetime import date, datetime
from lucca_timmi_timesheet_python_sdk.client_custom import ClientCustom
from lucca_timmi_timesheet_python_sdk.configuration import Configuration
from lucca_timmi_timesheet_python_sdk.api_client import ApiClient
from lucca_timmi_timesheet_python_sdk.type_util import copy_signature
from lucca_timmi_timesheet_python_sdk.apis.tags.reports_api import ReportsApi
from lucca_timmi_timesheet_python_sdk.apis.tags.time_entries_api import TimeEntriesApi
from lucca_timmi_timesheet_python_sdk.apis.tags.timesheets_api import TimesheetsApi
from lucca_timmi_timesheet_python_sdk.apis.tags.workflow_api import WorkflowApi



class LuccaTimmiTimesheet(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.reports: ReportsApi = ReportsApi(api_client)
        self.time_entries: TimeEntriesApi = TimeEntriesApi(api_client)
        self.timesheets: TimesheetsApi = TimesheetsApi(api_client)
        self.workflow: WorkflowApi = WorkflowApi(api_client)
