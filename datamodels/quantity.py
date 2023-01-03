from datamodels.datamodels import AbstractDataComponent, AllowedValues, SWEDataTypes


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
