import time
from dataclasses import dataclass

from oshdatacore.datamodels_core import DataComponentImpl, SWEDataTypes, AllowedTokens, AllowedValues


@dataclass(kw_only=True)
class BooleanComponent(DataComponentImpl):
    """
    The “Boolean” class is used to specify a scalar data component with a Boolean
    representation

    Attributes:
        name: The name of the component
        label: A human-readable label for the component
        definition: A URI that identifies the ontological definition of the component
        description: A description of the component
        value: The latest value of the component
        type: SWEDataTypes.BOOLEAN
    """
    value: bool = None
    type: str = SWEDataTypes.BOOLEAN


@dataclass(kw_only=True)
class TextComponent(DataComponentImpl):
    """
    The “Text” class is used to specify a component with a textual representation

    Attributes:
        name: The name of the component
        label: A human-readable label for the component
        definition: A URI that identifies the ontological definition of the component
        description: A description of the component
        constraint: limits the set of valid values
        value: The latest value of the component
        type: SWEDataTypes.TEXT
    """
    constraint: AllowedTokens = None
    value: str = None
    type = SWEDataTypes.TEXT

    def datastructure_to_dict(self):
        schema_dict = super().datastructure_to_dict()

        if self.constraint is not None:
            schema_dict['constraint'] = self.constraint.datastructure_to_dict()

        return schema_dict


@dataclass(kw_only=True)
class CategoryComponent(DataComponentImpl):
    """
    The “Category” class is used to specify a scalar data component with a categorical
    representation

    Attributes:
        name: The name of the component
        label: A human-readable label for the component
        definition: A URI that identifies the ontological definition of the component
        description: A description of the component
        codespace: dictionary listing and defining all possible values of the component. It is expected that the
            dictionary be referenced rather than included inline
        constraint: limits the set of valid values
        value: The latest value of the component
    """
    codespace: dict = None
    constraint: AllowedTokens = None
    type = SWEDataTypes.CATEGORY
    value: str = None

    def set_allowed_values(self, allowed_values: AllowedTokens):
        self.constraint = allowed_values

    def add_allowed_value(self, allowed_value: str):
        self.constraint.add_allowed_value(allowed_value)


@dataclass(kw_only=True)
class CountComponent(DataComponentImpl):
    """
    The “Count” class is used to specify a scalar data component with a discrete countable
    representation
    """

    type = SWEDataTypes.COUNT
    constraint: AllowedValues = None
    value: int = None

    def datastructure_to_dict(self):
        schema_dict = super().datastructure_to_dict()

        if self.constraint is not None:
            schema_dict['constraint'] = self.constraint.datastructure_to_dict()

        return schema_dict

    def set_allowed_values(self, allowed_values: AllowedValues):
        self.constraint = allowed_values

    def add_allowed_value(self, allowed_value: int):
        self.constraint.add_allowed_value(allowed_value)


@dataclass(kw_only=True)
class QuantityComponent(DataComponentImpl):
    """
    The “Quantity” class is used to specify a component with a continuous numerical
    representation
    """
    uom: str = None
    constraint: AllowedValues = None
    value: float = None
    type = SWEDataTypes.QUANTITY

    def datastructure_to_dict(self):
        schema_dict = super().datastructure_to_dict()

        if self.uom is not None:
            schema_dict['uom'] = self.uom

        if self.constraint is not None:
            schema_dict['constraint'] = self.constraint.datastructure_to_dict()

        return schema_dict

    def set_allowed_values(self, allowed_values: AllowedValues):
        self.constraint = allowed_values

    def add_allowed_value(self, allowed_value: int):
        self.constraint.add_allowed_value(allowed_value)


@dataclass(kw_only=True)
class TimeComponent(DataComponentImpl):
    """
    The “Time” class is used to specify a component with a date-time representation and
    whose value is projected along the axis of a temporal reference frame. This class is also
    necessary to specify that a time value is expressed in a calendar system.
    """

    definition: str = 'http://www.opengis.net/def/property/OGC/0/SamplingTime'
    reference_time: int = None
    local_frame: int = time.gmtime(0)
    uom: str = 'http://www.opengis.net/def/uom/ISO-8601/0/Gregorian'
    constraint: AllowedValues = None
    value: float = None
    type = SWEDataTypes.TIME

    def datastructure_to_dict(self):
        schema_dict = super().datastructure_to_dict()

        if self.uom is not None:
            schema_dict['uom'] = self.uom

        if self.constraint is not None:
            schema_dict['constraint'] = self.constraint.datastructure_to_dict()

        return schema_dict


# Record Components
class DataRecordComponent(DataComponentImpl):
    fields: list = []

    def __init__(self, name, label, definition, description=None):
        self.name = name
        self.label = label
        self.definition = definition
        self.description = description
        self.type = SWEDataTypes.DATA_RECORD
        self.fields = []

    def add_field(self, field):
        if issubclass(type(field), DataComponentImpl):
            self.fields.append(field)
            return field

    def datastructure_to_dict(self):
        schema_dict = super().datastructure_to_dict()

        field_dicts = []
        for field in self.fields:
            field_dicts.append(field.datastructure_to_dict())

        schema_dict['fields'] = field_dicts

        return schema_dict

    def get_fields(self):
        return self.fields

    def get_num_fields(self):
        return len(self.fields)


class VectorComponent(DataComponentImpl):
    referenceFrame: str
    localFrame: str
    coordinates: list[DataComponentImpl]
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

    def datastructure_to_dict(self):
        schema_dict = super().datastructure_to_dict()
        schema_dict['referenceFrame'] = self.referenceFrame
        schema_dict['localFrame'] = self.localFrame

        coord_dicts = []
        for coord in self.coordinates:
            coord_dicts.append(coord.datastructure_to_dict())

        schema_dict['coordinates'] = coord_dicts

        return schema_dict


# Block Components
class DataArrayComponent(DataComponentImpl):
    type = SWEDataTypes.DATA_ARRAY
    element_type: DataComponentImpl
    element_count: CountComponent  # This should be able to be set to another output that is Type=COUNT
    values: list[DataComponentImpl]

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

    def datastructure_to_dict(self):
        schema_dict = super().datastructure_to_dict()
        schema_dict['elementType'] = self.element_type.datastructure_to_dict()
        schema_dict['elementCount'] = self.element_count.datastructure_to_dict()

        value_dicts = []
        for value in self.values:
            value_dicts.append(value.datastructure_to_dict())

        schema_dict['values'] = value_dicts

        return schema_dict
