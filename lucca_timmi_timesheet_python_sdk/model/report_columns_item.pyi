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


class ReportColumnsItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            kind = schemas.StrSchema
            name = schemas.StrSchema
            category = schemas.StrSchema
            isRequired = schemas.BoolSchema
            isDefault = schemas.BoolSchema
            isPeriodic = schemas.BoolSchema
            __annotations__ = {
                "kind": kind,
                "name": name,
                "category": category,
                "isRequired": isRequired,
                "isDefault": isDefault,
                "isPeriodic": isPeriodic,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["kind"]) -> MetaOapg.properties.kind: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["category"]) -> MetaOapg.properties.category: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isRequired"]) -> MetaOapg.properties.isRequired: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isDefault"]) -> MetaOapg.properties.isDefault: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isPeriodic"]) -> MetaOapg.properties.isPeriodic: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["kind", "name", "category", "isRequired", "isDefault", "isPeriodic", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["kind"]) -> typing.Union[MetaOapg.properties.kind, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["category"]) -> typing.Union[MetaOapg.properties.category, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isRequired"]) -> typing.Union[MetaOapg.properties.isRequired, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isDefault"]) -> typing.Union[MetaOapg.properties.isDefault, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isPeriodic"]) -> typing.Union[MetaOapg.properties.isPeriodic, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["kind", "name", "category", "isRequired", "isDefault", "isPeriodic", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        kind: typing.Union[MetaOapg.properties.kind, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        category: typing.Union[MetaOapg.properties.category, str, schemas.Unset] = schemas.unset,
        isRequired: typing.Union[MetaOapg.properties.isRequired, bool, schemas.Unset] = schemas.unset,
        isDefault: typing.Union[MetaOapg.properties.isDefault, bool, schemas.Unset] = schemas.unset,
        isPeriodic: typing.Union[MetaOapg.properties.isPeriodic, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ReportColumnsItem':
        return super().__new__(
            cls,
            *args,
            kind=kind,
            name=name,
            category=category,
            isRequired=isRequired,
            isDefault=isDefault,
            isPeriodic=isPeriodic,
            _configuration=_configuration,
            **kwargs,
        )
