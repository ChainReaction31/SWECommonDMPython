from datamodels.datamodels import AbstractDataComponent, SWEDataTypes


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
