# coding: utf-8

"""
    Timmi Timesheet API

    Welcome on the documentation for the Timmi Timesheet API. 

    The version of the OpenAPI document: 1.0
    Contact: developers@lucca.fr
    Created by: https://www.lucca.fr
"""

from lucca_timmi_timesheet_python_sdk.paths.timmi_timesheet_api_reports.post import CreateBasedOnTemplateRaw
from lucca_timmi_timesheet_python_sdk.paths.timmi_timesheet_api_reports_report_id_download_csv.get import DownloadCsvReportRaw
from lucca_timmi_timesheet_python_sdk.paths.timmi_timesheet_api_reports_report_id_download_excel.get import DownloadExcelReportRaw


class ReportsApiRaw(
    CreateBasedOnTemplateRaw,
    DownloadCsvReportRaw,
    DownloadExcelReportRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
