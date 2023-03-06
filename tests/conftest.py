import pytest

from oshdatacore.component_implementations import BooleanComponent, TextComponent, CategoryComponent, CountComponent, \
    QuantityComponent, TimeComponent, DataRecordComponent, VectorComponent


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
