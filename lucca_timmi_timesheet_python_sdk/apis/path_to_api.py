import typing_extensions

from lucca_timmi_timesheet_python_sdk.paths import PathValues
from lucca_timmi_timesheet_python_sdk.apis.paths.api_v3_timeentries import ApiV3Timeentries
from lucca_timmi_timesheet_python_sdk.apis.paths.api_v3_timeentries_time_entry_id import ApiV3TimeentriesTimeEntryId
from lucca_timmi_timesheet_python_sdk.apis.paths.api_v3_timmitimesheets import ApiV3Timmitimesheets
from lucca_timmi_timesheet_python_sdk.apis.paths.api_v3_timmitimesheets_remindable import ApiV3TimmitimesheetsRemindable
from lucca_timmi_timesheet_python_sdk.apis.paths.timmi_services_workflow_remind import TimmiServicesWorkflowRemind
from lucca_timmi_timesheet_python_sdk.apis.paths.timmi_services_workflow_submit import TimmiServicesWorkflowSubmit
from lucca_timmi_timesheet_python_sdk.apis.paths.timmi_services_workflow_cancel import TimmiServicesWorkflowCancel
from lucca_timmi_timesheet_python_sdk.apis.paths.timmi_services_workflow_approve import TimmiServicesWorkflowApprove
from lucca_timmi_timesheet_python_sdk.apis.paths.timmi_services_workflow_deny import TimmiServicesWorkflowDeny
from lucca_timmi_timesheet_python_sdk.apis.paths.timmi_services_workflow_invalidate import TimmiServicesWorkflowInvalidate
from lucca_timmi_timesheet_python_sdk.apis.paths.timmi_timesheet_api_reports import TimmiTimesheetApiReports
from lucca_timmi_timesheet_python_sdk.apis.paths.timmi_timesheet_api_reports_report_id_download_csv import TimmiTimesheetApiReportsReportIdDownloadCsv
from lucca_timmi_timesheet_python_sdk.apis.paths.timmi_timesheet_api_reports_report_id_download_excel import TimmiTimesheetApiReportsReportIdDownloadExcel

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.API_V3_TIMEENTRIES: ApiV3Timeentries,
        PathValues.API_V3_TIMEENTRIES_TIME_ENTRY_ID: ApiV3TimeentriesTimeEntryId,
        PathValues.API_V3_TIMMITIMESHEETS: ApiV3Timmitimesheets,
        PathValues.API_V3_TIMMITIMESHEETS_REMINDABLE: ApiV3TimmitimesheetsRemindable,
        PathValues.TIMMI_SERVICES_WORKFLOW_REMIND: TimmiServicesWorkflowRemind,
        PathValues.TIMMI_SERVICES_WORKFLOW_SUBMIT: TimmiServicesWorkflowSubmit,
        PathValues.TIMMI_SERVICES_WORKFLOW_CANCEL: TimmiServicesWorkflowCancel,
        PathValues.TIMMI_SERVICES_WORKFLOW_APPROVE: TimmiServicesWorkflowApprove,
        PathValues.TIMMI_SERVICES_WORKFLOW_DENY: TimmiServicesWorkflowDeny,
        PathValues.TIMMI_SERVICES_WORKFLOW_INVALIDATE: TimmiServicesWorkflowInvalidate,
        PathValues.TIMMITIMESHEET_API_REPORTS: TimmiTimesheetApiReports,
        PathValues.TIMMITIMESHEET_API_REPORTS_REPORT_ID_DOWNLOADCSV: TimmiTimesheetApiReportsReportIdDownloadCsv,
        PathValues.TIMMITIMESHEET_API_REPORTS_REPORT_ID_DOWNLOADEXCEL: TimmiTimesheetApiReportsReportIdDownloadExcel,
    }
)

path_to_api = PathToApi(
    {
        PathValues.API_V3_TIMEENTRIES: ApiV3Timeentries,
        PathValues.API_V3_TIMEENTRIES_TIME_ENTRY_ID: ApiV3TimeentriesTimeEntryId,
        PathValues.API_V3_TIMMITIMESHEETS: ApiV3Timmitimesheets,
        PathValues.API_V3_TIMMITIMESHEETS_REMINDABLE: ApiV3TimmitimesheetsRemindable,
        PathValues.TIMMI_SERVICES_WORKFLOW_REMIND: TimmiServicesWorkflowRemind,
        PathValues.TIMMI_SERVICES_WORKFLOW_SUBMIT: TimmiServicesWorkflowSubmit,
        PathValues.TIMMI_SERVICES_WORKFLOW_CANCEL: TimmiServicesWorkflowCancel,
        PathValues.TIMMI_SERVICES_WORKFLOW_APPROVE: TimmiServicesWorkflowApprove,
        PathValues.TIMMI_SERVICES_WORKFLOW_DENY: TimmiServicesWorkflowDeny,
        PathValues.TIMMI_SERVICES_WORKFLOW_INVALIDATE: TimmiServicesWorkflowInvalidate,
        PathValues.TIMMITIMESHEET_API_REPORTS: TimmiTimesheetApiReports,
        PathValues.TIMMITIMESHEET_API_REPORTS_REPORT_ID_DOWNLOADCSV: TimmiTimesheetApiReportsReportIdDownloadCsv,
        PathValues.TIMMITIMESHEET_API_REPORTS_REPORT_ID_DOWNLOADEXCEL: TimmiTimesheetApiReportsReportIdDownloadExcel,
    }
)
