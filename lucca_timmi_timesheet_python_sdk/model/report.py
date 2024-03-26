# coding: utf-8

"""
    Timmi Timesheet API

    Welcome on the documentation for the Timmi Timesheet API. 

    The version of the OpenAPI document: 1.0
    Contact: developers@lucca.fr
    Created by: https://www.lucca.fr
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from lucca_timmi_timesheet_python_sdk import schemas  # noqa: F401


class Report(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    ## Status

The generation of a report content is a background process. As long as this process is not complete, the report status stays `pending`. Once the report is complete, its status is set to `done`. May an error be encountered while generating its content, then its status is set to `error`.

The report content can only be viewed and downloaded once it is `done`.

## Start & end dates

Start `startsOn` and end `endsOn` dates can be left `null`. In this case, default dates from the report-template are applied.

## Filters

Filters are usually set in the report-template. But these can be overriden for a given report.

## Fields
    """


    class MetaOapg:
        required = {
            "templateId",
        }
        
        class properties:
            templateId = schemas.StrSchema
            id = schemas.IntSchema
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "pending": "PENDING",
                        "done": "DONE",
                        "error": "ERROR",
                    }
                
                @schemas.classproperty
                def PENDING(cls):
                    return cls("pending")
                
                @schemas.classproperty
                def DONE(cls):
                    return cls("done")
                
                @schemas.classproperty
                def ERROR(cls):
                    return cls("error")
            name = schemas.StrSchema
            startsOn = schemas.DateSchema
            endsOn = schemas.DateSchema
            
            
            class filters(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            class properties:
                                kind = schemas.StrSchema
                                
                                
                                class values(
                                    schemas.ListSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        items = schemas.NumberSchema
                                
                                    def __new__(
                                        cls,
                                        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]]],
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                    ) -> 'values':
                                        return super().__new__(
                                            cls,
                                            arg,
                                            _configuration=_configuration,
                                        )
                                
                                    def __getitem__(self, i: int) -> MetaOapg.items:
                                        return super().__getitem__(i)
                                __annotations__ = {
                                    "kind": kind,
                                    "values": values,
                                }
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["kind"]) -> MetaOapg.properties.kind: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["values"]) -> MetaOapg.properties.values: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["kind", "values", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["kind"]) -> typing.Union[MetaOapg.properties.kind, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["values"]) -> typing.Union[MetaOapg.properties.values, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["kind", "values", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, ],
                            kind: typing.Union[MetaOapg.properties.kind, str, schemas.Unset] = schemas.unset,
                            values: typing.Union[MetaOapg.properties.values, list, tuple, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *args,
                                kind=kind,
                                values=values,
                                _configuration=_configuration,
                                **kwargs,
                            )
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'filters':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
        
            @staticmethod
            def columns() -> typing.Type['ReportColumns']:
                return ReportColumns
            __annotations__ = {
                "templateId": templateId,
                "id": id,
                "status": status,
                "name": name,
                "startsOn": startsOn,
                "endsOn": endsOn,
                "filters": filters,
                "columns": columns,
            }
    
    templateId: MetaOapg.properties.templateId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["templateId"]) -> MetaOapg.properties.templateId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startsOn"]) -> MetaOapg.properties.startsOn: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endsOn"]) -> MetaOapg.properties.endsOn: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["filters"]) -> MetaOapg.properties.filters: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["columns"]) -> 'ReportColumns': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["templateId", "id", "status", "name", "startsOn", "endsOn", "filters", "columns", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["templateId"]) -> MetaOapg.properties.templateId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startsOn"]) -> typing.Union[MetaOapg.properties.startsOn, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endsOn"]) -> typing.Union[MetaOapg.properties.endsOn, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["filters"]) -> typing.Union[MetaOapg.properties.filters, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["columns"]) -> typing.Union['ReportColumns', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["templateId", "id", "status", "name", "startsOn", "endsOn", "filters", "columns", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        templateId: typing.Union[MetaOapg.properties.templateId, str, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        startsOn: typing.Union[MetaOapg.properties.startsOn, str, date, schemas.Unset] = schemas.unset,
        endsOn: typing.Union[MetaOapg.properties.endsOn, str, date, schemas.Unset] = schemas.unset,
        filters: typing.Union[MetaOapg.properties.filters, list, tuple, schemas.Unset] = schemas.unset,
        columns: typing.Union['ReportColumns', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Report':
        return super().__new__(
            cls,
            *args,
            templateId=templateId,
            id=id,
            status=status,
            name=name,
            startsOn=startsOn,
            endsOn=endsOn,
            filters=filters,
            columns=columns,
            _configuration=_configuration,
            **kwargs,
        )

from lucca_timmi_timesheet_python_sdk.model.report_columns import ReportColumns
