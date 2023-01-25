import time

from oshdatacore.datamodels_core import SWEDataTypes


def test_bool_component(test_bool_comp):
    comp = test_bool_comp
    assert comp.name == 'test-bool'
    assert comp.label == 'Test Bool'
    assert comp.definition == 'www.test.org/test/bool'
    assert comp.description == 'Test Description'
    assert comp.type == SWEDataTypes.BOOLEAN
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


def test_text_component(test_text_comp):
    comp = test_text_comp
    assert comp.name == 'test-text'
    assert comp.label == 'Test Text'
    assert comp.definition == 'www.test.org/test/text'
    assert comp.description == 'Test Description'
    assert comp.type == SWEDataTypes.TEXT
    assert comp.extension is None
    assert comp.value is None


def test_category_component(test_category_comp):
    comp = test_category_comp
    assert comp.name == 'test-category'
    assert comp.label == 'Test Category'
    assert comp.definition == 'www.test.org/test/category'
    assert comp.description == 'Test Description'
    assert comp.type == SWEDataTypes.CATEGORY
    assert comp.extension is None
    assert comp.value is None


def test_count_component(test_count_comp):
    comp = test_count_comp
    assert comp.name == 'test-count'
    assert comp.label == 'Test Count'
    assert comp.definition == 'www.test.org/test/count'
    assert comp.description == 'Test Description'
    assert comp.type == SWEDataTypes.COUNT
    assert comp.extension is None
    assert comp.value is None


def test_quantity_component(test_quantity_comp):
    comp = test_quantity_comp
    assert comp.name == 'test-quantity'
    assert comp.label == 'Test Quantity'
    assert comp.definition == 'www.test.org/test/quantity'
    assert comp.description == 'Test Description'
    assert comp.type == SWEDataTypes.QUANTITY
    assert comp.extension is None
    assert comp.value is None


def test_time_component(test_time_comp):
    comp = test_time_comp
    assert comp.name == 'test-time'
    assert comp.label == 'Test Time'
    assert comp.definition == 'http://www.opengis.net/def/property/OGC/0/SamplingTime'
    assert comp.description == 'Test Description'
    assert comp.type == SWEDataTypes.TIME
    assert comp.extension is None
    assert comp.value is None
    assert comp.uom == 'http://www.opengis.net/def/uom/ISO-8601/0/Gregorian'
    assert comp.local_frame == time.gmtime(0)
