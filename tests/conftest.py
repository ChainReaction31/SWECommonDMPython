import pytest

from oshdatacore.component_implementations import BooleanComponent


@pytest.fixture
def test_bool_comp():
    comp = BooleanComponent(name='test-bool', label='Test Bool', definition='www.test.org/test/bool',
                            description='Test Description')
    return comp
