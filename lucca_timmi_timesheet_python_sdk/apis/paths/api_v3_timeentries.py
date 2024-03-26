from lucca_timmi_timesheet_python_sdk.paths.api_v3_timeentries.get import ApiForget
from lucca_timmi_timesheet_python_sdk.paths.api_v3_timeentries.put import ApiForput
from lucca_timmi_timesheet_python_sdk.paths.api_v3_timeentries.post import ApiForpost
from lucca_timmi_timesheet_python_sdk.paths.api_v3_timeentries.delete import ApiFordelete


class ApiV3Timeentries(
    ApiForget,
    ApiForput,
    ApiForpost,
    ApiFordelete,
):
    pass
