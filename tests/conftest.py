import pytest

from swe_common_data_models_python.component_implementations import BooleanComponent, TextComponent, CategoryComponent, CountComponent, \
    QuantityComponent, TimeComponent, DataRecordComponent, VectorComponent, DataArrayComponent


@pytest.fixture
def test_bool_comp():
    comp = BooleanComponent(name='test-bool', label='Test Bool', definition='www.test.org/test/bool',
                            description='Test Description')
    return comp


@pytest.fixture
def test_text_comp():
    comp = TextComponent(name='test-text', label='Test Text', definition='www.test.org/test/text',
                         description='Test Description')
    return comp


@pytest.fixture
def test_category_comp():
    comp = CategoryComponent(name='test-category', label='Test Category', definition='www.test.org/test/category',
                             description='Test Description')
    return comp


@pytest.fixture
def test_count_comp():
    comp = CountComponent(name='test-count', label='Test Count', definition='www.test.org/test/count',
                          description='Test Description')
    return comp


@pytest.fixture
def test_quantity_comp():
    comp = QuantityComponent(name='test-quantity', label='Test Quantity', definition='www.test.org/test/quantity',
                             description='Test Description')
    return comp


@pytest.fixture
def test_time_comp():
    comp = TimeComponent(name='test-time', label='Test Time', description='Test Description')
    return comp


@pytest.fixture
def test_comp_datarecord():
    comp = DataRecordComponent(name='test-datarecord', label='Test DataRecord', description='Test Description',
                               definition='www.test.org/test/datarecord')
    return comp


@pytest.fixture
def test_comp_vector():
    comp = VectorComponent(name='test-vector', label='Test Vector', description='Test Description',
                           definition='www.test.org/test/vector',
                           reference_frame='http://www.opengis.net/def/crs/EPSG/0/9705', local_frame='#SENSOR_FRAME')
    lat = QuantityComponent(name='lat', label='Test Lat', definition='www.test.org/test/lat', uom='deg')
    lon = QuantityComponent(name='lon', label='Test Lon', definition='www.test.org/test/lon', uom='deg')
    alt = QuantityComponent(name='alt', label='Test Alt', definition='www.test.org/test/alt', uom='m')
    comp.add_coord('Lat', lat)
    comp.add_coord('Lon', lon)
    comp.add_coord('Alt', alt)

    return comp


@pytest.fixture
def test_comp_data_array():
    comp = DataArrayComponent(name='test-data-array', label='Test DataArray', description='Test Description',
                              definition='www.test.org/test/data-array')
    element_type = QuantityComponent(name='array-element', label='Array Element',
                                     definition='www.test.org/test/array-element-qty')
    element_count = CountComponent(name='array-count', label='Array Count', definition='www.test.org/test/array-count',
                                   value=3)
    comp.set_component_template_and_size(element_count.get_value(), element_type)
    return comp


@pytest.fixture
def test_nested_comp_data_array_1():
    comp = DataArrayComponent(name='test-data-array', label='Test DataArray', description='Test Description',
                              definition='www.test.org/test/data-array')
    element_type = DataRecordComponent(name='array-element', label='Array Element',
                                       definition='www.test.org/test/array-element-dr')
    element_type.add_field(TextComponent(name='f1', label='Test Field', definition='www.test.org/test/field'))
    element_type.add_field(QuantityComponent(name='f2', label='Test Field', definition='www.test.org/test/field'))
    element_count = CountComponent(name='array-count', label='Array Count', definition='www.test.org/test/array-count',
                                   value=2)
    comp.set_component_template_and_size(element_count.get_value(), element_type)
    return comp


@pytest.fixture
def test_nested_comp_data_array_2():
    comp = DataArrayComponent(name='test-data-array', label='Test DataArray', description='Test Description',
                              definition='www.test.org/test/data-array')
    element_type = VectorComponent(name='array-element', label='Array Element',
                                   definition='www.test.org/test/array-element-v',
                                   reference_frame='http://www.opengis.net/def/crs/EPSG/0/9705',
                                   local_frame='#SENSOR_FRAME')
    element_type.add_coord('Lat', QuantityComponent(name='lat', label='Test Lat', definition='www.test.org/test/lat'))
    element_type.add_coord('Lon', QuantityComponent(name='lon', label='Test Lon', definition='www.test.org/test/lon'))
    element_type.add_coord('Alt', QuantityComponent(name='alt', label='Test Alt', definition='www.test.org/test/alt'))

    element_count = CountComponent(name='array-count', label='Array Count', definition='www.test.org/test/array-count',
                                   value=2)
    comp.set_component_template_and_size(element_count.get_value(), element_type)
    return comp


@pytest.fixture
def test_nested_comp_data_array_3():
    comp = DataArrayComponent(name='test-data-array', label='Test DataArray', description='Test Description',
                              definition='www.test.org/test/data-array')
    element_type = DataArrayComponent(name='array-element', label='Array Element',
                                      definition='www.test.org/test/array-element-da')
    element_type.set_component_template_and_size(1080, CountComponent(name='array-element', label='Array Element',
                                                                   definition='www.test.org/test/array-element-text'))
    element_count = CountComponent(name='array-count', label='Array Count', definition='www.test.org/test/array-count',
                                   value=1920)
    comp.set_component_template_and_size(element_count.get_value(), element_type)
    return comp
