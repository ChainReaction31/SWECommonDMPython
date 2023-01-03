import time
from datamodels.datamodels import AbstractDataComponent, AllowedValues, SWEDataTypes


class TimeComponent(AbstractDataComponent):
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

    def as_schemaful_dict(self):
        schema_dict = super().as_schemaful_dict()

        if self.uom is not None:
            schema_dict['uom'] = self.uom

        if self.constraint is not None:
            schema_dict['constraint'] = self.constraint.as_schemaful_dict()

        return schema_dict
