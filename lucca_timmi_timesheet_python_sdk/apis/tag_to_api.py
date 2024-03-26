import typing_extensions

from lucca_timmi_timesheet_python_sdk.apis.tags import TagValues
from lucca_timmi_timesheet_python_sdk.apis.tags.time_entries_api import TimeEntriesApi
from lucca_timmi_timesheet_python_sdk.apis.tags.workflow_api import WorkflowApi
from lucca_timmi_timesheet_python_sdk.apis.tags.reports_api import ReportsApi
from lucca_timmi_timesheet_python_sdk.apis.tags.timesheets_api import TimesheetsApi
from lucca_timmi_timesheet_python_sdk.apis.tags.activities_api import ActivitiesApi
from lucca_timmi_timesheet_python_sdk.apis.tags.attendance_api import AttendanceApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.TIME_ENTRIES: TimeEntriesApi,
        TagValues.WORKFLOW: WorkflowApi,
        TagValues.REPORTS: ReportsApi,
        TagValues.TIMESHEETS: TimesheetsApi,
        TagValues.ACTIVITIES: ActivitiesApi,
        TagValues.ATTENDANCE: AttendanceApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.TIME_ENTRIES: TimeEntriesApi,
        TagValues.WORKFLOW: WorkflowApi,
        TagValues.REPORTS: ReportsApi,
        TagValues.TIMESHEETS: TimesheetsApi,
        TagValues.ACTIVITIES: ActivitiesApi,
        TagValues.ATTENDANCE: AttendanceApi,
    }
)
