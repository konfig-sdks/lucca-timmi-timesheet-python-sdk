# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from lucca_timmi_timesheet_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    API_V3_TIMEENTRIES = "/api/v3/timeentries"
    API_V3_TIMEENTRIES_TIME_ENTRY_ID = "/api/v3/timeentries/{timeEntryId}"
    API_V3_TIMMITIMESHEETS = "/api/v3/timmitimesheets"
    API_V3_TIMMITIMESHEETS_REMINDABLE = "/api/v3/timmitimesheets/remindable"
    TIMMI_SERVICES_WORKFLOW_REMIND = "/timmi/services/workflow/remind"
    TIMMI_SERVICES_WORKFLOW_SUBMIT = "/timmi/services/workflow/submit"
    TIMMI_SERVICES_WORKFLOW_CANCEL = "/timmi/services/workflow/cancel"
    TIMMI_SERVICES_WORKFLOW_APPROVE = "/timmi/services/workflow/approve"
    TIMMI_SERVICES_WORKFLOW_DENY = "/timmi/services/workflow/deny"
    TIMMI_SERVICES_WORKFLOW_INVALIDATE = "/timmi/services/workflow/invalidate"
    TIMMITIMESHEET_API_REPORTS = "/timmi-timesheet/api/reports"
    TIMMITIMESHEET_API_REPORTS_REPORT_ID_DOWNLOADCSV = "/timmi-timesheet/api/reports/{reportId}/download-csv"
    TIMMITIMESHEET_API_REPORTS_REPORT_ID_DOWNLOADEXCEL = "/timmi-timesheet/api/reports/{reportId}/download-excel"
