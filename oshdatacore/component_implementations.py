import time

from datamodels_core import DataComponentImpl, SWEDataTypes, AllowedTokens, AllowedValues


class BooleanComponent(DataComponentImpl):
    """
    The “Boolean” class is used to specify a scalar data component with a Boolean
    representation
    """
    value: bool
    type: SWEDataTypes.BOOLEAN

    def __int__(self, name, label, definition, description=None):
        self.name = name
        self.label = label
        self.definition = definition
        self.description = description
        self.type = SWEDataTypes.BOOLEAN


class TextComponent(DataComponentImpl):
    """
    The “Text” class is used to specify a component with a textual representation
    """
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

    def datastructure_to_dict(self):
        schema_dict = super().datastructure_to_dict()

        if self.constraint is not None:
            schema_dict['constraint'] = self.constraint.datastructure_to_dict()

        return schema_dict


class CategoryComponent(DataComponentImpl):
    """
    Unimplemented
    """


class CountComponent(DataComponentImpl):
    """
    The “Count” class is used to specify a scalar data component with a discrete countable
    representation
    """
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

    def datastructure_to_dict(self):
        schema_dict = super().datastructure_to_dict()

        if self.constraint is not None:
            schema_dict['constraint'] = self.constraint.datastructure_to_dict()

        return schema_dict


class QuantityComponent(DataComponentImpl):
    """
    The “Quantity” class is used to specify a component with a continuous numerical
    representation
    """
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

    def datastructure_to_dict(self):
        schema_dict = super().datastructure_to_dict()

        if self.uom is not None:
            schema_dict['uom'] = self.uom

        if self.constraint is not None:
            schema_dict['constraint'] = self.constraint.datastructure_to_dict()

        return schema_dict


class TimeComponent(DataComponentImpl):
    """
    The “Time” class is used to specify a component with a date-time representation and
    whose value is projected along the axis of a temporal reference frame. This class is also
    necessary to specify that a time value is expressed in a calendar system.
    """
    reference_time: int
    local_frame: int
    uom: str
    constraint: AllowedValues
    value: float
    type = SWEDataTypes.TIME

    def __init__(self, name, label, definition='http://www.opengis.net/def/property/OGC/0/SamplingTime',
                 description=None, constraint=None,
                 uom='http://www.opengis.net/def/uom/ISO-8601/0/Gregorian'):
        self.local_frame = time.gmtime(0)
        self.uom = uom
        self.name = name
        self.type = SWEDataTypes.TIME
        self.constraint = constraint
        self.label = label
        self.definition = definition
        self.description = description

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
