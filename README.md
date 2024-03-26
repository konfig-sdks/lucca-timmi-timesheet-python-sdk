<div align="left">

[![Visit Lucca](./header.png)](https://lucca-hr.com)

# Lucca<a id="lucca"></a>

Welcome on the documentation for the Timmi Timesheet API.



</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`luccatimmitimesheet.reports.create_based_on_template`](#luccatimmitimesheetreportscreate_based_on_template)
  * [`luccatimmitimesheet.reports.download_csv_report`](#luccatimmitimesheetreportsdownload_csv_report)
  * [`luccatimmitimesheet.reports.download_excel_report`](#luccatimmitimesheetreportsdownload_excel_report)
  * [`luccatimmitimesheet.time_entries.create_multiple`](#luccatimmitimesheettime_entriescreate_multiple)
  * [`luccatimmitimesheet.time_entries.delete_multiple`](#luccatimmitimesheettime_entriesdelete_multiple)
  * [`luccatimmitimesheet.time_entries.get_by_id`](#luccatimmitimesheettime_entriesget_by_id)
  * [`luccatimmitimesheet.time_entries.list_time_entries`](#luccatimmitimesheettime_entrieslist_time_entries)
  * [`luccatimmitimesheet.time_entries.remove_by_id`](#luccatimmitimesheettime_entriesremove_by_id)
  * [`luccatimmitimesheet.time_entries.update_by_id`](#luccatimmitimesheettime_entriesupdate_by_id)
  * [`luccatimmitimesheet.time_entries.update_multiple`](#luccatimmitimesheettime_entriesupdate_multiple)
  * [`luccatimmitimesheet.timesheets.list`](#luccatimmitimesheettimesheetslist)
  * [`luccatimmitimesheet.timesheets.list_due`](#luccatimmitimesheettimesheetslist_due)
  * [`luccatimmitimesheet.workflow.approve_timesheets_by_id`](#luccatimmitimesheetworkflowapprove_timesheets_by_id)
  * [`luccatimmitimesheet.workflow.cancel_timesheet_by_id`](#luccatimmitimesheetworkflowcancel_timesheet_by_id)
  * [`luccatimmitimesheet.workflow.deny_timesheet_by_id`](#luccatimmitimesheetworkflowdeny_timesheet_by_id)
  * [`luccatimmitimesheet.workflow.invalidate_timesheet_by_id`](#luccatimmitimesheetworkflowinvalidate_timesheet_by_id)
  * [`luccatimmitimesheet.workflow.send_reminder_email`](#luccatimmitimesheetworkflowsend_reminder_email)
  * [`luccatimmitimesheet.workflow.submit_timesheet`](#luccatimmitimesheetworkflowsubmit_timesheet)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Lucca&serviceName=Timmi%20Timesheet&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from lucca_timmi_timesheet_python_sdk import LuccaTimmiTimesheet, ApiException

luccatimmitimesheet = LuccaTimmiTimesheet(
    authorization="YOUR_API_KEY",
)

try:
    # Create a new Report
    create_based_on_template_response = (
        luccatimmitimesheet.reports.create_based_on_template(
            template_id="string_example",
            id=1,
            status="pending",
            name="string_example",
            starts_on="1970-01-01",
            ends_on="1970-01-01",
            filters=[{}],
            columns=[{}],
        )
    )
    print(create_based_on_template_response)
except ApiException as e:
    print("Exception when calling ReportsApi.create_based_on_template: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from lucca_timmi_timesheet_python_sdk import LuccaTimmiTimesheet, ApiException

luccatimmitimesheet = LuccaTimmiTimesheet(
    authorization="YOUR_API_KEY",
)


async def main():
    try:
        # Create a new Report
        create_based_on_template_response = (
            await luccatimmitimesheet.reports.acreate_based_on_template(
                template_id="string_example",
                id=1,
                status="pending",
                name="string_example",
                starts_on="1970-01-01",
                ends_on="1970-01-01",
                filters=[{}],
                columns=[{}],
            )
        )
        print(create_based_on_template_response)
    except ApiException as e:
        print("Exception when calling ReportsApi.create_based_on_template: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from lucca_timmi_timesheet_python_sdk import LuccaTimmiTimesheet, ApiException

luccatimmitimesheet = LuccaTimmiTimesheet(
    authorization="YOUR_API_KEY",
)

try:
    # Create a new Report
    create_based_on_template_response = (
        luccatimmitimesheet.reports.raw.create_based_on_template(
            template_id="string_example",
            id=1,
            status="pending",
            name="string_example",
            starts_on="1970-01-01",
            ends_on="1970-01-01",
            filters=[{}],
            columns=[{}],
        )
    )
    pprint(create_based_on_template_response.body)
    pprint(create_based_on_template_response.body["template_id"])
    pprint(create_based_on_template_response.body["id"])
    pprint(create_based_on_template_response.body["status"])
    pprint(create_based_on_template_response.body["name"])
    pprint(create_based_on_template_response.body["starts_on"])
    pprint(create_based_on_template_response.body["ends_on"])
    pprint(create_based_on_template_response.body["filters"])
    pprint(create_based_on_template_response.body["columns"])
    pprint(create_based_on_template_response.headers)
    pprint(create_based_on_template_response.status)
    pprint(create_based_on_template_response.round_trip_time)
except ApiException as e:
    print("Exception when calling ReportsApi.create_based_on_template: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `luccatimmitimesheet.reports.create_based_on_template`<a id="luccatimmitimesheetreportscreate_based_on_template"></a>

<!-- theme: info -->
> This endpoint does not adhere to the "v3 API endpoints" principles. The "fields" query parameter is not supported, but all fields are systematically returned.

A report can only be created based on an existing report-template. So you first need to retrieve the report-template unique identifier `templateId`.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_based_on_template_response = (
    luccatimmitimesheet.reports.create_based_on_template(
        template_id="string_example",
        id=1,
        status="pending",
        name="string_example",
        starts_on="1970-01-01",
        ends_on="1970-01-01",
        filters=[{}],
        columns=[{}],
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### template_id: `str`<a id="template_id-str"></a>

##### id: `int`<a id="id-int"></a>

##### status: `str`<a id="status-str"></a>

##### name: `str`<a id="name-str"></a>

##### starts_on: `date`<a id="starts_on-date"></a>

##### ends_on: `date`<a id="ends_on-date"></a>

##### filters: List[`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`]<a id="filters-listdictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

##### columns: [`ReportColumns`](./lucca_timmi_timesheet_python_sdk/type/report_columns.py)<a id="columns-reportcolumnslucca_timmi_timesheet_python_sdktypereport_columnspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Report`](./lucca_timmi_timesheet_python_sdk/type/report.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Report`](./lucca_timmi_timesheet_python_sdk/pydantic/report.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/timmi-timesheet/api/reports` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `luccatimmitimesheet.reports.download_csv_report`<a id="luccatimmitimesheetreportsdownload_csv_report"></a>

<!-- theme: info -->
> This endpoint does not adhere to the "v3 API endpoints" principles.

Download a report content as an CSV file `.csv`.

Column delimiter and numbers formating depends on the authentified user's culture.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
download_csv_report_response = luccatimmitimesheet.reports.download_csv_report(
    report_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### report_id: `int`<a id="report_id-int"></a>

Identifier of the report.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/timmi-timesheet/api/reports/{reportId}/download-csv` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `luccatimmitimesheet.reports.download_excel_report`<a id="luccatimmitimesheetreportsdownload_excel_report"></a>

<!-- theme: info -->
> This endpoint does not adhere to the "v3 API endpoints" principles.

Download a report content as an Excel file `.xls`.

Column delimiter and numbers formating depends on the authentified user's culture.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
download_excel_report_response = luccatimmitimesheet.reports.download_excel_report(
    report_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### report_id: `int`<a id="report_id-int"></a>

Identifier of the report.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/timmi-timesheet/api/reports/{reportId}/download-excel` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `luccatimmitimesheet.time_entries.create_multiple`<a id="luccatimmitimesheettime_entriescreate_multiple"></a>

<!-- theme: warning --> 
>#### Warning
> This endpoint will soon be deprecated, please use [Timmi Timesheet v4 API](Timmi-Timesheet.yaml/paths/~1timmi-timesheet~1services~1time-entries/put)

You can create a single or multiple TimeEntries for a given user.

Beware, a new TimeEntry cannot intersect with a submitted or approved timesheet.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_multiple_response = luccatimmitimesheet.time_entries.create_multiple(
    body=None,
    id=1,
    starts_at="2022-01-01T08:00:00",
    duration="03:45:00",
    unit=0,
    ends_at="1970-01-01T00:00:00.00Z",
    owner_id=1,
    author_id=1,
    created_at="1970-01-01T00:00:00.00Z",
    creation_source=2,
    modifier_id=1,
    modified_at=1,
    layer=1,
    axis_sections=[{}],
    comment=None,
    time_type_id=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

Unique identifier for this object.

##### starts_at: `datetime`<a id="starts_at-datetime"></a>

The timeEntry start date and time. Please do NOT send any offset/timezone information (\\\"Z\\\", \\\"+01:00\\\", etc...).

##### duration: `str`<a id="duration-str"></a>

Format: d.hh:mm:ss. Max: \\\"1.00:00:00\\\" (ie 24 hours).

##### unit: `int`<a id="unit-int"></a>

0: Days (eg \\\"1/2 day\\\"). 1: Hours (eg \\\"8h15min\\\"). 2: Time (eg \\\"23:45:00\\\").

##### ends_at: `datetime`<a id="ends_at-datetime"></a>

##### owner_id: `int`<a id="owner_id-int"></a>

The user's unique identifier.

##### author_id: `int`<a id="author_id-int"></a>

Identifier of the user who initially created this TimeEntry.

##### created_at: `datetime`<a id="created_at-datetime"></a>

##### creation_source: `int`<a id="creation_source-int"></a>

0: Fallback on theoretical TimeEntries. 1: Application of bookmarked week. 2: Manual creation. 3: Import

##### modifier_id: `int`<a id="modifier_id-int"></a>

The unique identifier of the user who last updated the TimeEntry.

##### modified_at: `int`<a id="modified_at-int"></a>

Date and time when TimeEntry was last modified.

##### layer: `int`<a id="layer-int"></a>

0: Actual. 1: Theoretical

##### axis_sections: List[`AxisSection`]<a id="axis_sections-listaxissection"></a>

When not in activity mode, send an empty array, or do not serialize this property.

##### comment: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./lucca_timmi_timesheet_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="comment-unionbool-date-datetime-dict-float-int-list-str-nonelucca_timmi_timesheet_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


Only used on activities (TimeEntries w/ AxisSections).

##### time_type_id: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./lucca_timmi_timesheet_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="time_type_id-unionbool-date-datetime-dict-float-int-list-str-nonelucca_timmi_timesheet_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TimeEntriesCreateMultipleRequest`](./lucca_timmi_timesheet_python_sdk/type/time_entries_create_multiple_request.py)
Create a single of multiple TimeEntry (toggle body type).

#### 🔄 Return<a id="🔄-return"></a>

[`TimeEntriesCreateMultipleResponse`](./lucca_timmi_timesheet_python_sdk/pydantic/time_entries_create_multiple_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/timeentries` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `luccatimmitimesheet.time_entries.delete_multiple`<a id="luccatimmitimesheettime_entriesdelete_multiple"></a>

<!-- theme: warning --> 
>#### Warning
> This endpoint will soon be deprecated, please use [Timmi Timesheet v4 API](Timmi-Timesheet.yaml/paths/~1timmi-timesheet~1services~1time-entries/put)

Delete one or several TimeEntries. The "id" field of each TimeEntry must be sent and correspond to an existing TimeEntry.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
luccatimmitimesheet.time_entries.delete_multiple(
    body=[
        {
            "id": 0,
        }
    ],
)
```

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TimeEntriesDeleteMultipleRequest`](./lucca_timmi_timesheet_python_sdk/type/time_entries_delete_multiple_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/timeentries` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `luccatimmitimesheet.time_entries.get_by_id`<a id="luccatimmitimesheettime_entriesget_by_id"></a>

Retrieve a single TimeEntry identified by its unique identifier.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = luccatimmitimesheet.time_entries.get_by_id(
    time_entry_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### time_entry_id: `int`<a id="time_entry_id-int"></a>

Identifier of the TimeEntry.

#### 🔄 Return<a id="🔄-return"></a>

[`TimeEntriesGetByIdResponse`](./lucca_timmi_timesheet_python_sdk/pydantic/time_entries_get_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/timeentries/{timeEntryId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `luccatimmitimesheet.time_entries.list_time_entries`<a id="luccatimmitimesheettime_entrieslist_time_entries"></a>

Retrieve a list of TimeEntries.

The `startsAt` query parameter can operate comparisons with a given date-time value:
- `?startsAt=2021-01-01`: strict equality.
- `?startsAt=since,2021-01-01`: greater than or equal.
- `?startsAt=until,2021-01-01`: lower than or equal.
- `?startsAt=between,2021-01-01,2021-01-31`: comprised between two dates.

To retrieve the total count of all TimeEntries (on all pages), please include the field `?field=collection.count`.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_time_entries_response = luccatimmitimesheet.time_entries.list_time_entries(
    paging="100,0",
    owner_id=[None],
    starts_at="between,2021-01-01,2021-02-01",
    axis_sections_id=[None],
    axis_sections_code=[None],
    modified_at="since,2021-01-01T08:45:23Z",
    archived_at="since,2021-01-01T08:45:23Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### paging: `str`<a id="paging-str"></a>

{offset},{limit}. Defaults to 0,1000.

##### owner_id: List[[`Union[bool, date, datetime, dict, float, int, list, str, None]`](./lucca_timmi_timesheet_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)]<a id="owner_id-listunionbool-date-datetime-dict-float-int-list-str-nonelucca_timmi_timesheet_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

User's identifier

##### starts_at: `str`<a id="starts_at-str"></a>

{comparator},{date-time}

##### axis_sections_id: List[[`Union[bool, date, datetime, dict, float, int, list, str, None]`](./lucca_timmi_timesheet_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)]<a id="axis_sections_id-listunionbool-date-datetime-dict-float-int-list-str-nonelucca_timmi_timesheet_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Filter on a comma-separated list of AxisSections identifiers.

##### axis_sections_code: List[[`Union[bool, date, datetime, dict, float, int, list, str, None]`](./lucca_timmi_timesheet_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)]<a id="axis_sections_code-listunionbool-date-datetime-dict-float-int-list-str-nonelucca_timmi_timesheet_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Filter on a comma-separated list of AxisSections codes.

##### modified_at: `str`<a id="modified_at-str"></a>

{comparator},{date-time}

##### archived_at: `str`<a id="archived_at-str"></a>

{comparator},{date-time}

#### 🔄 Return<a id="🔄-return"></a>

[`TimeEntriesListTimeEntriesResponse`](./lucca_timmi_timesheet_python_sdk/pydantic/time_entries_list_time_entries_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/timeentries` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `luccatimmitimesheet.time_entries.remove_by_id`<a id="luccatimmitimesheettime_entriesremove_by_id"></a>

<!-- theme: warning --> 
>#### Warning
> This endpoint will soon be deprecated, please use [Timmi Timesheet v4 API](Timmi-Timesheet.yaml/paths/~1timmi-timesheet~1services~1time-entries/put)

Delete a single TimeEntry. Deletion is irrevocable.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
luccatimmitimesheet.time_entries.remove_by_id(
    time_entry_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### time_entry_id: `int`<a id="time_entry_id-int"></a>

Identifier of the TimeEntry.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/timeentries/{timeEntryId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `luccatimmitimesheet.time_entries.update_by_id`<a id="luccatimmitimesheettime_entriesupdate_by_id"></a>

<!-- theme: warning --> 
>#### Warning
> This endpoint will soon be deprecated, please use [Timmi Timesheet v4 API](Timmi-Timesheet.yaml/paths/~1timmi-timesheet~1services~1time-entries/put)

Update fields of a single TimeEntry identified by its unique id.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_by_id_response = luccatimmitimesheet.time_entries.update_by_id(
    starts_at="2022-01-01T08:00:00",
    duration="03:45:00",
    unit=0,
    owner_id=1,
    time_entry_id=1,
    id=1,
    ends_at="1970-01-01T00:00:00.00Z",
    author_id=1,
    created_at="1970-01-01T00:00:00.00Z",
    creation_source=2,
    modifier_id=1,
    modified_at=1,
    layer=1,
    axis_sections=[{}],
    comment=None,
    time_type_id=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### starts_at: `datetime`<a id="starts_at-datetime"></a>

The timeEntry start date and time. Please do NOT send any offset/timezone information (\\\"Z\\\", \\\"+01:00\\\", etc...).

##### duration: `str`<a id="duration-str"></a>

Format: d.hh:mm:ss. Max: \\\"1.00:00:00\\\" (ie 24 hours).

##### unit: `int`<a id="unit-int"></a>

0: Days (eg \\\"1/2 day\\\"). 1: Hours (eg \\\"8h15min\\\"). 2: Time (eg \\\"23:45:00\\\").

##### owner_id: `int`<a id="owner_id-int"></a>

The user's unique identifier.

##### time_entry_id: `int`<a id="time_entry_id-int"></a>

Identifier of the TimeEntry.

##### id: `int`<a id="id-int"></a>

Unique identifier for this object.

##### ends_at: `datetime`<a id="ends_at-datetime"></a>

##### author_id: `int`<a id="author_id-int"></a>

Identifier of the user who initially created this TimeEntry.

##### created_at: `datetime`<a id="created_at-datetime"></a>

##### creation_source: `int`<a id="creation_source-int"></a>

0: Fallback on theoretical TimeEntries. 1: Application of bookmarked week. 2: Manual creation. 3: Import

##### modifier_id: `int`<a id="modifier_id-int"></a>

The unique identifier of the user who last updated the TimeEntry.

##### modified_at: `int`<a id="modified_at-int"></a>

Date and time when TimeEntry was last modified.

##### layer: `int`<a id="layer-int"></a>

0: Actual. 1: Theoretical

##### axis_sections: List[`AxisSection`]<a id="axis_sections-listaxissection"></a>

When not in activity mode, send an empty array, or do not serialize this property.

##### comment: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./lucca_timmi_timesheet_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="comment-unionbool-date-datetime-dict-float-int-list-str-nonelucca_timmi_timesheet_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


Only used on activities (TimeEntries w/ AxisSections).

##### time_type_id: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./lucca_timmi_timesheet_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="time_type_id-unionbool-date-datetime-dict-float-int-list-str-nonelucca_timmi_timesheet_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TimeEntry`](./lucca_timmi_timesheet_python_sdk/type/time_entry.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TimeEntriesUpdateByIdResponse`](./lucca_timmi_timesheet_python_sdk/pydantic/time_entries_update_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/timeentries/{timeEntryId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `luccatimmitimesheet.time_entries.update_multiple`<a id="luccatimmitimesheettime_entriesupdate_multiple"></a>

<!-- theme: warning --> 
>#### Warning
> This endpoint will soon be deprecated, please use [Timmi Timesheet v4 API](Timmi-Timesheet.yaml/paths/~1timmi-timesheet~1services~1time-entries/put)

Update one or several TimeEntries. The "id" field must be sent and correspond to an existing TimeEntry.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_multiple_response = luccatimmitimesheet.time_entries.update_multiple(
    body=None,
    id=1,
    starts_at="2022-01-01T08:00:00",
    duration="03:45:00",
    unit=0,
    ends_at="1970-01-01T00:00:00.00Z",
    owner_id=1,
    author_id=1,
    created_at="1970-01-01T00:00:00.00Z",
    creation_source=2,
    modifier_id=1,
    modified_at=1,
    layer=1,
    axis_sections=[{}],
    comment=None,
    time_type_id=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

Unique identifier for this object.

##### starts_at: `datetime`<a id="starts_at-datetime"></a>

The timeEntry start date and time. Please do NOT send any offset/timezone information (\\\"Z\\\", \\\"+01:00\\\", etc...).

##### duration: `str`<a id="duration-str"></a>

Format: d.hh:mm:ss. Max: \\\"1.00:00:00\\\" (ie 24 hours).

##### unit: `int`<a id="unit-int"></a>

0: Days (eg \\\"1/2 day\\\"). 1: Hours (eg \\\"8h15min\\\"). 2: Time (eg \\\"23:45:00\\\").

##### ends_at: `datetime`<a id="ends_at-datetime"></a>

##### owner_id: `int`<a id="owner_id-int"></a>

The user's unique identifier.

##### author_id: `int`<a id="author_id-int"></a>

Identifier of the user who initially created this TimeEntry.

##### created_at: `datetime`<a id="created_at-datetime"></a>

##### creation_source: `int`<a id="creation_source-int"></a>

0: Fallback on theoretical TimeEntries. 1: Application of bookmarked week. 2: Manual creation. 3: Import

##### modifier_id: `int`<a id="modifier_id-int"></a>

The unique identifier of the user who last updated the TimeEntry.

##### modified_at: `int`<a id="modified_at-int"></a>

Date and time when TimeEntry was last modified.

##### layer: `int`<a id="layer-int"></a>

0: Actual. 1: Theoretical

##### axis_sections: List[`AxisSection`]<a id="axis_sections-listaxissection"></a>

When not in activity mode, send an empty array, or do not serialize this property.

##### comment: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./lucca_timmi_timesheet_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="comment-unionbool-date-datetime-dict-float-int-list-str-nonelucca_timmi_timesheet_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


Only used on activities (TimeEntries w/ AxisSections).

##### time_type_id: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./lucca_timmi_timesheet_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="time_type_id-unionbool-date-datetime-dict-float-int-list-str-nonelucca_timmi_timesheet_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TimeEntriesUpdateMultipleRequest`](./lucca_timmi_timesheet_python_sdk/type/time_entries_update_multiple_request.py)
You can either update a single or multiple TimeEntries. Pick the correct body type accordingly.

#### 🔄 Return<a id="🔄-return"></a>

[`TimeEntriesUpdateMultipleResponse`](./lucca_timmi_timesheet_python_sdk/pydantic/time_entries_update_multiple_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/timeentries` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `luccatimmitimesheet.timesheets.list`<a id="luccatimmitimesheettimesheetslist"></a>

List all timesheets satisfying query filters.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = luccatimmitimesheet.timesheets.list(
    owner_id=[None],
    starts_on="between,2022-01-01,2022-02-01",
    status=[None],
    ends_on="until,2022-01-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### owner_id: List[[`OwnerId`](./lucca_timmi_timesheet_python_sdk/type/owner_id.py)]<a id="owner_id-listowneridlucca_timmi_timesheet_python_sdktypeowner_idpy"></a>

User's identifier.

##### starts_on: `str`<a id="starts_on-str"></a>

Filter on the start date of the timesheet.

##### status: List[[`Status`](./lucca_timmi_timesheet_python_sdk/type/status.py)]<a id="status-liststatuslucca_timmi_timesheet_python_sdktypestatuspy"></a>

Filter on the timesheet workflow status.

##### ends_on: `str`<a id="ends_on-str"></a>

Filter on the end date of the timesheet.

#### 🔄 Return<a id="🔄-return"></a>

[`TimesheetsListResponse`](./lucca_timmi_timesheet_python_sdk/pydantic/timesheets_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/timmitimesheets` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `luccatimmitimesheet.timesheets.list_due`<a id="luccatimmitimesheettimesheetslist_due"></a>

List timesheet that are not yet submitted (status: 0). 
You must filter on either `ownerIds`, `managerIds` or `legalEntityIds`.
As long as a timesheet is not submitted, its unique identifier is equal to zero.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_due_response = luccatimmitimesheet.timesheets.list_due(
    owner_ids=[1],
    legal_entity_ids=[1],
    manager_ids=[1],
    start="1970-01-01",
    end="1970-01-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### owner_ids: List[`int`]<a id="owner_ids-listint"></a>

List unique identifier of submitters.

##### legal_entity_ids: List[`int`]<a id="legal_entity_ids-listint"></a>

List unique identifier of submitters' legal establishments.

##### manager_ids: List[`int`]<a id="manager_ids-listint"></a>

List unique identifier of submitters' manager.

##### start: `date`<a id="start-date"></a>

Prevent older timesheets to be returned.

##### end: `date`<a id="end-date"></a>

Prevent earlier timesheets to be returned (date excluded). Defaults to today when not sent.

#### 🔄 Return<a id="🔄-return"></a>

[`TimesheetsListDueResponse`](./lucca_timmi_timesheet_python_sdk/pydantic/timesheets_list_due_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/timmitimesheets/remindable` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `luccatimmitimesheet.workflow.approve_timesheets_by_id`<a id="luccatimmitimesheetworkflowapprove_timesheets_by_id"></a>

<!-- theme: warning --> 
>#### Warning
> This endpoint will soon be deprecated, please use [Timmi Timesheet v4 API](../reference/Timmi-Timesheet.yaml/paths/~1timmi-timesheet~1api~1timesheets~1{id}~1approve/post)

Multiple approvals can be required, depending on the configuration.

Once all approvals needed are satisfied, the timesheet status is set to `2: Approved`.

Comprised TimeEntries can only be modified by rejecting the timesheet through the "invalidate" operation.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
approve_timesheets_by_id_response = (
    luccatimmitimesheet.workflow.approve_timesheets_by_id(
        timesheets=[
            {
                "id": 1,
            }
        ],
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### timesheets: [`WorkflowApproveTimesheetsByIdRequestTimesheets`](./lucca_timmi_timesheet_python_sdk/type/workflow_approve_timesheets_by_id_request_timesheets.py)<a id="timesheets-workflowapprovetimesheetsbyidrequesttimesheetslucca_timmi_timesheet_python_sdktypeworkflow_approve_timesheets_by_id_request_timesheetspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WorkflowApproveTimesheetsByIdRequest`](./lucca_timmi_timesheet_python_sdk/type/workflow_approve_timesheets_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WorkflowSendReminderEmailResponse`](./lucca_timmi_timesheet_python_sdk/pydantic/workflow_send_reminder_email_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/timmi/services/workflow/approve` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `luccatimmitimesheet.workflow.cancel_timesheet_by_id`<a id="luccatimmitimesheetworkflowcancel_timesheet_by_id"></a>

<!-- theme: warning --> 
>#### Warning
> This endpoint will soon be deprecated, please use [Timmi Timesheet v4 API](../reference/Timmi-Timesheet.yaml/paths/~1timmi-timesheet~1api~1timesheets~1{id}~1cancel/post)

Cancel a timesheet's submission. Can only be achieved by the original submitter as long as the timesheet's not approved.

Sets the timesheet status to `3` (rejected).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
cancel_timesheet_by_id_response = luccatimmitimesheet.workflow.cancel_timesheet_by_id(
    timesheets=[
        {
            "id": 1,
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### timesheets: [`WorkflowCancelTimesheetByIdRequestTimesheets`](./lucca_timmi_timesheet_python_sdk/type/workflow_cancel_timesheet_by_id_request_timesheets.py)<a id="timesheets-workflowcanceltimesheetbyidrequesttimesheetslucca_timmi_timesheet_python_sdktypeworkflow_cancel_timesheet_by_id_request_timesheetspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WorkflowCancelTimesheetByIdRequest`](./lucca_timmi_timesheet_python_sdk/type/workflow_cancel_timesheet_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WorkflowSendReminderEmailResponse`](./lucca_timmi_timesheet_python_sdk/pydantic/workflow_send_reminder_email_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/timmi/services/workflow/cancel` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `luccatimmitimesheet.workflow.deny_timesheet_by_id`<a id="luccatimmitimesheetworkflowdeny_timesheet_by_id"></a>

<!-- theme: warning --> 
>#### Warning
> This endpoint will soon be deprecated, please use [Timmi Timesheet v4 API](../reference/Timmi-Timesheet.yaml/paths/~1timmi-timesheet~1api~1timesheets~1{id}~1deny/post)

Denies a submitted timesheet pending approval. Sets its status to `3` (rejected) and a new timesheet may be submitted for this User and [StartsOn - EndsOn[.

Comment is mandatory.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
deny_timesheet_by_id_response = luccatimmitimesheet.workflow.deny_timesheet_by_id(
    timesheets=[
        {
            "id": 1,
            "comment": "comment_example",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### timesheets: [`WorkflowDenyTimesheetByIdRequestTimesheets`](./lucca_timmi_timesheet_python_sdk/type/workflow_deny_timesheet_by_id_request_timesheets.py)<a id="timesheets-workflowdenytimesheetbyidrequesttimesheetslucca_timmi_timesheet_python_sdktypeworkflow_deny_timesheet_by_id_request_timesheetspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WorkflowDenyTimesheetByIdRequest`](./lucca_timmi_timesheet_python_sdk/type/workflow_deny_timesheet_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WorkflowSendReminderEmailResponse`](./lucca_timmi_timesheet_python_sdk/pydantic/workflow_send_reminder_email_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/timmi/services/workflow/deny` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `luccatimmitimesheet.workflow.invalidate_timesheet_by_id`<a id="luccatimmitimesheetworkflowinvalidate_timesheet_by_id"></a>

<!-- theme: warning --> 
>#### Warning
> This endpoint will soon be deprecated, please use [Timmi Timesheet v4 API](../reference/Timmi-Timesheet.yaml/paths/~1timmi-timesheet~1api~1timesheets~1{id}~1invalidate/post)

Rejects an approved timesheet. Sets its status to `3` (rejected). A new timesheet may then be submitted for this User and [StartsOn - EndsOn[.

Comment is mandatory.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
invalidate_timesheet_by_id_response = (
    luccatimmitimesheet.workflow.invalidate_timesheet_by_id(
        timesheets=[
            {
                "id": 1,
            }
        ],
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### timesheets: [`WorkflowInvalidateTimesheetByIdRequestTimesheets`](./lucca_timmi_timesheet_python_sdk/type/workflow_invalidate_timesheet_by_id_request_timesheets.py)<a id="timesheets-workflowinvalidatetimesheetbyidrequesttimesheetslucca_timmi_timesheet_python_sdktypeworkflow_invalidate_timesheet_by_id_request_timesheetspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WorkflowInvalidateTimesheetByIdRequest`](./lucca_timmi_timesheet_python_sdk/type/workflow_invalidate_timesheet_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WorkflowSendReminderEmailResponse`](./lucca_timmi_timesheet_python_sdk/pydantic/workflow_send_reminder_email_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/timmi/services/workflow/invalidate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `luccatimmitimesheet.workflow.send_reminder_email`<a id="luccatimmitimesheetworkflowsend_reminder_email"></a>

Remind user of a due timesheet. Sends him/her an email.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
send_reminder_email_response = luccatimmitimesheet.workflow.send_reminder_email(
    timesheets=[
        {
            "starts_at": "1970-01-01",
            "ends_at": "1970-01-01",
            "owner_id": 1,
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### timesheets: [`WorkflowSendReminderEmailRequestTimesheets`](./lucca_timmi_timesheet_python_sdk/type/workflow_send_reminder_email_request_timesheets.py)<a id="timesheets-workflowsendreminderemailrequesttimesheetslucca_timmi_timesheet_python_sdktypeworkflow_send_reminder_email_request_timesheetspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WorkflowSendReminderEmailRequest`](./lucca_timmi_timesheet_python_sdk/type/workflow_send_reminder_email_request.py)
Timesheets are identified by startsAt, endsAt & ownerId.

#### 🔄 Return<a id="🔄-return"></a>

[`WorkflowSendReminderEmailResponse`](./lucca_timmi_timesheet_python_sdk/pydantic/workflow_send_reminder_email_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/timmi/services/workflow/remind` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `luccatimmitimesheet.workflow.submit_timesheet`<a id="luccatimmitimesheetworkflowsubmit_timesheet"></a>

<!-- theme: warning -->
> #### Warning
> This endpoint will soon be deprecated, please use [Timmi Timesheet v4 API](../reference/Timmi-Timesheet.yaml/paths/~1timmi-timesheet~1api~1timesheets~1submit/post)

Timesheet is created and its status is set to `1` (pending approval). In some cases, timesheet may then be automatically approved (`status: 2`), depending on the application settings.

Once submitted, all comprised TimeEntries for user can no longer be modified. In order to be able to modify them, the timesheet must first be rejected through `cancel`, `deny` or `invalidate` operations (depends on the current timesheet status).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
submit_timesheet_response = luccatimmitimesheet.workflow.submit_timesheet(
    timesheets=[
        {
            "starts_at": "1970-01-01",
            "ends_at": "1970-01-01",
            "owner_id": 1,
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### timesheets: [`WorkflowSubmitTimesheetRequestTimesheets`](./lucca_timmi_timesheet_python_sdk/type/workflow_submit_timesheet_request_timesheets.py)<a id="timesheets-workflowsubmittimesheetrequesttimesheetslucca_timmi_timesheet_python_sdktypeworkflow_submit_timesheet_request_timesheetspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WorkflowSubmitTimesheetRequest`](./lucca_timmi_timesheet_python_sdk/type/workflow_submit_timesheet_request.py)
Timesheets are identified by startsAt, endsAt & ownerId.

#### 🔄 Return<a id="🔄-return"></a>

[`WorkflowSendReminderEmailResponse`](./lucca_timmi_timesheet_python_sdk/pydantic/workflow_send_reminder_email_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/timmi/services/workflow/submit` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
