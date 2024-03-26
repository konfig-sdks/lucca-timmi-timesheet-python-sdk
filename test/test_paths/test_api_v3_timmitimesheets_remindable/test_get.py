# coding: utf-8

"""
    Timmi Timesheet API

    Welcome on the documentation for the Timmi Timesheet API. 

    The version of the OpenAPI document: 1.0
    Contact: developers@lucca.fr
    Created by: https://www.lucca.fr
"""

import unittest
from unittest.mock import patch

import urllib3

import lucca_timmi_timesheet_python_sdk
from lucca_timmi_timesheet_python_sdk.paths.api_v3_timmitimesheets_remindable import get
from lucca_timmi_timesheet_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApiV3TimmitimesheetsRemindable(ApiTestMixin, unittest.TestCase):
    """
    ApiV3TimmitimesheetsRemindable unit test stubs
        List due timesheets
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
