from oshdatacore.component_implementations import BooleanComponent
from oshdatacore.datamodels_core import SWEDataTypes


def test_bool_component(test_bool_comp):
    comp = test_bool_comp
    assert comp.name == 'test-bool'
    assert comp.label == 'Test Bool'
    assert comp.definition == 'www.test.org/test/bool'
    assert comp.description == 'Test Description'
    assert comp.type == SWEDataTypes.BOOLEAN.value
    assert comp.extension is None
    assert comp.value is None


def test_bool_to_dict(test_bool_comp):
    comp = test_bool_comp
    comp_dict = comp.datastructure_to_dict()
    print(comp_dict)
    assert comp_dict['name'] == 'test-bool'
    assert comp_dict['label'] == 'Test Bool'
    assert comp_dict['definition'] == 'www.test.org/test/bool'
    assert comp_dict['description'] == 'Test Description'

