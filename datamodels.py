from abc import ABC
from enum import Enum
from numbers import Real


class SWEDataTypes(Enum):
    DATA_RECORD = 'DataRecord'
    DATA_ARRAY = 'DataArray'
    VECTOR = 'Vector'
    TEXT = 'Text'
    QUANTITY = 'Quantity'
    CATEGORY = 'Category'


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


class CountComponent(AbstractDataComponent):
    constraint: AllowedValues
    value: int
    type = SWEDataTypes.QUANTITY

    def __init__(self, name, label, definition, description=None, constraint=None):
        self.name = name
        self.type = SWEDataTypes.QUANTITY
        self.constraint = constraint
        self.label = label
        self.definition = definition
        self.description = description

    def as_schemaful_dict(self):
        schema_dict = super().as_schemaful_dict()

        if self.constraint is not None:
            schema_dict['constraint'] = self.constraint.as_schemaful_dict()

        return schema_dict


class QuantityComponent(AbstractDataComponent):
    uom: str
    constraint: AllowedValues
    value: float
    type = SWEDataTypes.QUANTITY

    def __init__(self, name, label, definition, uom=None, description=None, constraint=None):
        self.name = name
        self.type = SWEDataTypes.QUANTITY
        self.uom = uom
        self.constraint = constraint
        self.label = label
        self.definition = definition
        self.description = description

    def as_schemaful_dict(self):
        schema_dict = super().as_schemaful_dict()

        if self.uom is not None:
            schema_dict['uom'] = self.uom

        if self.constraint is not None:
            schema_dict['constraint'] = self.constraint.as_schemaful_dict()

        return schema_dict


class TextComponent(AbstractDataComponent):
    constraint: AllowedTokens
    value: str
    type = SWEDataTypes.TEXT

    def __init__(self, name, label, definition, description=None, constraint=None):
        self.name = name
        self.type = SWEDataTypes.TEXT
        self.constraint = constraint
        self.label = label
        self.definition = definition
        self.description = description

    def as_schemaful_dict(self):
        schema_dict = super().as_schemaful_dict()

        if self.constraint is not None:
            schema_dict['constraint'] = self.constraint.as_schemaful_dict()

        return schema_dict


""" Record Components:
    * DataRecord
    * Vector
"""


class DataRecordComponent(AbstractDataComponent):
    fields: list = []

    def __init__(self, name, label, definition, description=None):
        self.name = name
        self.label = label
        self.definition = definition
        self.description = description
        self.type = SWEDataTypes.DATA_RECORD
        self.fields = []

    def add_field(self, field):
        self.fields.append(field)
        return field

    def as_schemaful_dict(self):
        schema_dict = super().as_schemaful_dict()

        field_dicts = []
        for field in self.fields:
            field_dicts.append(field.as_schemaful_dict())

        schema_dict['fields'] = field_dicts

        return schema_dict


class VectorComponent(AbstractDataComponent):
    referenceFrame: str
    localFrame: str
    coordinates: list[AbstractDataComponent]
    type = SWEDataTypes.VECTOR

    def __init__(self, name, label, definition, description=None, reference_frame=None, local_frame=None):
        self.name = name
        self.label = label
        self.referenceFrame = reference_frame
        self.localFrame = local_frame
        self.coordinates = []
        self.definition = definition
        self.description = description

    def add_coord(self, coordinate):
        self.coordinates.append(coordinate)

    def as_schemaful_dict(self):
        schema_dict = super().as_schemaful_dict()
        schema_dict['referenceFrame'] = self.referenceFrame
        schema_dict['localFrame'] = self.localFrame

        coord_dicts = []
        for coord in self.coordinates:
            coord_dicts.append(coord.as_schemaful_dict())

        schema_dict['coordinates'] = coord_dicts

        return schema_dict


""" Block Components:
    * DataArray
    * Matrix (unimplemented)
    * DataStream (unimplemented)
"""


class DataArrayComponent(AbstractDataComponent):
    type = SWEDataTypes.DATA_ARRAY
    element_type: AbstractDataComponent
    element_count: CountComponent  # This should be able to be set to another output that is Type=COUNT
    values: list[AbstractDataComponent]

    def __init__(self, name, label, definition, element_count, element_type, description=None):
        self.name = name
        self.label = label
        self.definition = definition
        self.description = description
        self.element_type = element_type
        self.element_count = element_count
        self.values = []

    def add_value(self, value):
        self.values.append(value)

    def as_schemaful_dict(self):
        schema_dict = super().as_schemaful_dict()
        schema_dict['elementType'] = self.element_type.as_schemaful_dict()
        schema_dict['elementCount'] = self.element_count.as_schemaful_dict()

        value_dicts = []
        for value in self.values:
            value_dicts.append(value.as_schemaful_dict())

        schema_dict['values'] = value_dicts

        return schema_dict
