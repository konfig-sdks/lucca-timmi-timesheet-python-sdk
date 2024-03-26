# coding: utf-8

"""
    Timmi Timesheet API

    Welcome on the documentation for the Timmi Timesheet API. 

    The version of the OpenAPI document: 1.0
    Contact: developers@lucca.fr
    Created by: https://www.lucca.fr
"""

import unittest

import os
from pprint import pprint
from lucca_timmi_timesheet_python_sdk import LuccaTimmiTimesheet

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        luccatimmitimesheet = LuccaTimmiTimesheet(
        
                        authorization = 'YOUR_API_KEY',
        )
        self.assertIsNotNone(luccatimmitimesheet)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
