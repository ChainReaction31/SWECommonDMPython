from dataclasses import dataclass
from enum import Enum
from numbers import Real


class SWEDataTypes(Enum):
    """
        Data types as defined in the SWE Common Data Model.

        NOTE: The list here may not be complete,
        and those listed may not be implemented though support for every type is planned
    """
    BOOLEAN = 'Boolean'
    TEXT = 'Text'
    CATEGORY = 'Category',
    COUNT = 'Count'
    QUANTITY = 'Quantity'
    TIME = 'Time',
    DATA_RECORD = 'DataRecord'
    VECTOR = 'Vector'
    DATA_ARRAY = 'DataArray'


class AllowedTokens:

    def __init__(self, value: list[str] = None, pattern: str = None):
        """
        This class allows defining the constraint either by enumerating a list of allowed values by
        using one or more “value” attributes and/or by specifying a pattern that the value must
        match. The value must then either be one of the enumerated tokens or match the pattern.
        :param value: A list of allowed values
        :param pattern: A regular expression that the value must match
        """
        self.value: set[str] = value
        self.pattern: str = pattern

    def datastructure_to_dict(self):
        schema_dict = dict()
        if self.value is not None:
            schema_dict['value'] = self.value
        if self.pattern is not None:
            schema_dict['pattern'] = self.pattern

        return schema_dict

    def add_value(self, value: str):
        if value is not None:
            self.value.add(value)
        return self.value

    def remove_value(self, value: str):
        if self.value is not None:
            self.value.discard(value)
        return self.value


class AllowedValues:

    def __init__(self, value: list[Real] = None, interval: range = None, significant_figures: int = None):
        """
        This class allows defining the constraint either by enumerating a list of allowed values by
        using one or more “value” attributes and/or by specifying a pattern that the value must
        match. The value must then either be one of the enumerated tokens or match the pattern.
        :param value: A list of allowed real number values
        :param interval: A range of allowed real number values
        :param significant_figures: Limits the total number of digits included in the represented number.
        Only applies to decimals
        """
        self.value: set[Real] = value
        self.interval: range = interval
        self.significant_figures: int = significant_figures

    def datastructure_to_dict(self):
        schema_dict = dict()
        if self.value is not None:
            schema_dict['value'] = self.value
        if self.interval is not None:
            schema_dict['interval'] = self.interval
        if self.significant_figures is not None:
            schema_dict['significantFigures'] = self.significant_figures

        return schema_dict

    def add_value(self, value: Real):
        if value is not None:
            self.value.add(value)
        return self.value

    def remove_value(self, value: Real):
        if self.value is not None:
            self.value.discard(value)
        return self.value


@dataclass
class SWEImpl:
    """
        This class should not be instantiated, just inherited from
    """
    extension: str
    """
        The “extension” attribute is used as a container for future extensions.
    """


@dataclass
class SweIdentifiableImpl(SWEImpl):
    """
        This class should not be instantiated, just inherited from
    """
    identifier: str
    """
        The optional “identifier” attribute allows assigning a unique identifier to the component,
        so that it can be referenced later on. It can be used, for example, when defining the
        unique identifier of a universal constant.
    """
    label: str
    """
        The label attribute is meant to hold a short, descriptive name
    """
    description: str
    """
       Description can carry any length of plain text 
    """


@dataclass
class DataComponentImpl(SweIdentifiableImpl):
    """
        This class should not be instantiated, just inherited from
    """
    name: str
    """
        The name attribute is meant to hold a short, descriptive name
    """
    definition: str
    """
        The “definition” attribute identifies the property (often an observed property in our
        context) that the data component represents by using a scoped name. It should map to a
        controlled term defined in an (web accessible) dictionary, registry or ontology. Such
        terms provide the formal textual definition agreed upon by one or more communities,
        eventually illustrated by pictures and diagrams as well as additional semantic information
        such as relationships to units and other concepts, ontological mappings, etc.
    """
    optional: True
    """
        The “optional” attribute is an optional flag indicating if the component value can be
        omitted in the data stream. It is only meaningful if the component is used as a schema
        descriptor (i.e. not for a component containing an inline value). It is ‘false’ by default.
    """
    updatable: True
    """
        The “updatable” attribute is an optional flag indicating if the component value is fixed or
        can be updated. It is only applicable if the data component is used to define the input of a
        process (i.e. when used to define the input or parameter of a service, process or sensor,
        but not when used to define the content of a dataset).
    """

    def datastructure_to_dict(self):
        schema_dict = dict([
            ('name', self.name),
            ('type', self.type.value),
            ('label', self.label),
            ('definition', self.definition),
            ('description', self.description)
        ])
        return schema_dict


""" Basic Data Types:
    * Boolean (Unimplemented)
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
