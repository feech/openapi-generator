# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
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

from petstore_api import schemas  # noqa: F401


class Drawing(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def mainShape() -> typing.Type['Shape']:
                return Shape
        
            @staticmethod
            def shapeOrNull() -> typing.Type['ShapeOrNull']:
                return ShapeOrNull
        
            @staticmethod
            def nullableShape() -> typing.Type['NullableShape']:
                return NullableShape
            
            
            class shapes(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Shape']:
                        return Shape
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['Shape'], typing.List['Shape']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'shapes':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Shape':
                    return super().__getitem__(i)
            __annotations__ = {
                "mainShape": mainShape,
                "shapeOrNull": shapeOrNull,
                "nullableShape": nullableShape,
                "shapes": shapes,
            }
        
        @staticmethod
        def additional_properties() -> typing.Type['Fruit']:
            return Fruit
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mainShape"]) -> 'Shape': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shapeOrNull"]) -> 'ShapeOrNull': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nullableShape"]) -> 'NullableShape': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shapes"]) -> MetaOapg.properties.shapes: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> 'Fruit': ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["mainShape"], typing_extensions.Literal["shapeOrNull"], typing_extensions.Literal["nullableShape"], typing_extensions.Literal["shapes"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mainShape"]) -> typing.Union['Shape', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shapeOrNull"]) -> typing.Union['ShapeOrNull', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nullableShape"]) -> typing.Union['NullableShape', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shapes"]) -> typing.Union[MetaOapg.properties.shapes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union['Fruit', schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["mainShape"], typing_extensions.Literal["shapeOrNull"], typing_extensions.Literal["nullableShape"], typing_extensions.Literal["shapes"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        mainShape: typing.Union['Shape', schemas.Unset] = schemas.unset,
        shapeOrNull: typing.Union['ShapeOrNull', schemas.Unset] = schemas.unset,
        nullableShape: typing.Union['NullableShape', schemas.Unset] = schemas.unset,
        shapes: typing.Union[MetaOapg.properties.shapes, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: 'Fruit',
    ) -> 'Drawing':
        return super().__new__(
            cls,
            *args,
            mainShape=mainShape,
            shapeOrNull=shapeOrNull,
            nullableShape=nullableShape,
            shapes=shapes,
            _configuration=_configuration,
            **kwargs,
        )

from petstore_api.model.fruit import Fruit
from petstore_api.model.nullable_shape import NullableShape
from petstore_api.model.shape import Shape
from petstore_api.model.shape_or_null import ShapeOrNull
