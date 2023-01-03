from datamodels.datamodels import AbstractDataComponent, SWEDataTypes


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
