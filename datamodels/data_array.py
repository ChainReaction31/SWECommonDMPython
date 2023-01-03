from datamodels.datamodels import AbstractDataComponent, SWEDataTypes
from count import CountComponent


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
