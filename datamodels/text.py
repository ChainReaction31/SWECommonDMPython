from datamodels.datamodels import AbstractDataComponent, AllowedTokens, SWEDataTypes


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
