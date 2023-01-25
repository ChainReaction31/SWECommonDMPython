import pytest

from oshdatacore.component_implementations import BooleanComponent, TextComponent, CategoryComponent, CountComponent, \
    QuantityComponent, TimeComponent


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
