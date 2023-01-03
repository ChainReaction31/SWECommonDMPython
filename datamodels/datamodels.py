import time
from abc import ABC
from enum import Enum
from numbers import Real


class SWEDataTypes(Enum):
    DATA_RECORD = 'DataRecord'
    DATA_ARRAY = 'DataArray'
    VECTOR = 'Vector'
    TEXT = 'Text'
    QUANTITY = 'Quantity'
    CATEGORY = 'Category',
    TIME = 'Time'


class AllowedTokens:
    value: list[str]
    pattern: str

    def as_schemaful_dict(self):
        schema_dict = dict()
        if self.value is not None:
            schema_dict['value'] = self.value
        if self.pattern is not None:
            schema_dict['pattern'] = self.pattern

        return schema_dict


class AllowedValues:
    value: Real
    interval: range
    significantFigures: int

    def as_schemaful_dict(self):
        schema_dict = dict()
        if self.value is not None:
            schema_dict['value'] = self.value
        if self.interval is not None:
            schema_dict['interval'] = self.interval
        if self.significantFigures is not None:
            schema_dict['significantFigures'] = self.significantFigures

        return schema_dict


class AbstractSWE(ABC):
    extension: str = ""


class AbstractSweIdentifiable(AbstractSWE, ABC):
    identifier: str
    label: str
    description: str


class AbstractDataComponent(AbstractSweIdentifiable, ABC):
    name: str
    type: SWEDataTypes
    definition: str
    optional: True
    updatable: True

    def set_name(self, name):
        self.name = name

    def set_type(self, type: SWEDataTypes):
        self.type = type

    def as_schemaful_dict(self):
        schema_dict = dict([
            ('name', self.name),
            ('type', self.type.value),
            ('label', self.label),
            ('definition', self.definition),
            ('description', self.description)
        ])
        return schema_dict


""" Basic Data Types:
    * Boolean
    * Text
    * Category(unimplemented)
    * Count
    * Quantity
    * Time(unimplemented)
"""

""" Record Components:
    * DataRecord
    * Vector
"""

""" Block Components:
    * DataArray
    * Matrix (unimplemented)
    * DataStream (unimplemented)
"""
