operation_parameter_map = {
    '/timmi-timesheet/api/reports-POST': {
        'parameters': [
            {
                'name': 'templateId'
            },
            {
                'name': 'id'
            },
            {
                'name': 'status'
            },
            {
                'name': 'name'
            },
            {
                'name': 'startsOn'
            },
            {
                'name': 'endsOn'
            },
            {
                'name': 'filters'
            },
            {
                'name': 'columns'
            },
        ]
    },
    '/timmi-timesheet/api/reports/{reportId}/download-csv-GET': {
        'parameters': [
            {
                'name': 'reportId'
            },
        ]
    },
    '/timmi-timesheet/api/reports/{reportId}/download-excel-GET': {
        'parameters': [
            {
                'name': 'reportId'
            },
        ]
    },
    '/api/v3/timeentries-POST': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'startsAt'
            },
            {
                'name': 'duration'
            },
            {
                'name': 'unit'
            },
            {
                'name': 'endsAt'
            },
            {
                'name': 'ownerId'
            },
            {
                'name': 'authorId'
            },
            {
                'name': 'createdAt'
            },
            {
                'name': 'creationSource'
            },
            {
                'name': 'modifierId'
            },
            {
                'name': 'modifiedAt'
            },
            {
                'name': 'layer'
            },
            {
                'name': 'axisSections'
            },
            {
                'name': 'comment'
            },
            {
                'name': 'timeTypeId'
            },
        ]
    },
    '/api/v3/timeentries-DELETE': {
        'parameters': [
        ]
    },
    '/api/v3/timeentries/{timeEntryId}-GET': {
        'parameters': [
            {
                'name': 'timeEntryId'
            },
        ]
    },
    '/api/v3/timeentries-GET': {
        'parameters': [
            {
                'name': 'paging'
            },
            {
                'name': 'ownerId'
            },
            {
                'name': 'startsAt'
            },
            {
                'name': 'axisSections.id'
            },
            {
                'name': 'axisSections.code'
            },
            {
                'name': 'modifiedAt'
            },
            {
                'name': 'archivedAt'
            },
        ]
    },
    '/api/v3/timeentries/{timeEntryId}-DELETE': {
        'parameters': [
            {
                'name': 'timeEntryId'
            },
        ]
    },
    '/api/v3/timeentries/{timeEntryId}-PUT': {
        'parameters': [
            {
                'name': 'startsAt'
            },
            {
                'name': 'duration'
            },
            {
                'name': 'unit'
            },
            {
                'name': 'ownerId'
            },
            {
                'name': 'timeEntryId'
            },
            {
                'name': 'id'
            },
            {
                'name': 'endsAt'
            },
            {
                'name': 'authorId'
            },
            {
                'name': 'createdAt'
            },
            {
                'name': 'creationSource'
            },
            {
                'name': 'modifierId'
            },
            {
                'name': 'modifiedAt'
            },
            {
                'name': 'layer'
            },
            {
                'name': 'axisSections'
            },
            {
                'name': 'comment'
            },
            {
                'name': 'timeTypeId'
            },
        ]
    },
    '/api/v3/timeentries-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'startsAt'
            },
            {
                'name': 'duration'
            },
            {
                'name': 'unit'
            },
            {
                'name': 'endsAt'
            },
            {
                'name': 'ownerId'
            },
            {
                'name': 'authorId'
            },
            {
                'name': 'createdAt'
            },
            {
                'name': 'creationSource'
            },
            {
                'name': 'modifierId'
            },
            {
                'name': 'modifiedAt'
            },
            {
                'name': 'layer'
            },
            {
                'name': 'axisSections'
            },
            {
                'name': 'comment'
            },
            {
                'name': 'timeTypeId'
            },
        ]
    },
    '/api/v3/timmitimesheets-GET': {
        'parameters': [
            {
                'name': 'ownerId'
            },
            {
                'name': 'startsOn'
            },
            {
                'name': 'status'
            },
            {
                'name': 'endsOn'
            },
        ]
    },
    '/api/v3/timmitimesheets/remindable-GET': {
        'parameters': [
            {
                'name': 'ownerIds'
            },
            {
                'name': 'legalEntityIds'
            },
            {
                'name': 'managerIds'
            },
            {
                'name': 'start'
            },
            {
                'name': 'end'
            },
        ]
    },
    '/timmi/services/workflow/approve-POST': {
        'parameters': [
            {
                'name': 'timesheets'
            },
        ]
    },
    '/timmi/services/workflow/cancel-POST': {
        'parameters': [
            {
                'name': 'timesheets'
            },
        ]
    },
    '/timmi/services/workflow/deny-POST': {
        'parameters': [
            {
                'name': 'timesheets'
            },
        ]
    },
    '/timmi/services/workflow/invalidate-POST': {
        'parameters': [
            {
                'name': 'timesheets'
            },
        ]
    },
    '/timmi/services/workflow/remind-POST': {
        'parameters': [
            {
                'name': 'timesheets'
            },
        ]
    },
    '/timmi/services/workflow/submit-POST': {
        'parameters': [
            {
                'name': 'timesheets'
            },
        ]
    },
};