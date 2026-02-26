import pytest

from project.math_utils import multiply, safe_divide


def test_multiply():
    assert multiply(3, 5) == 15
    assert multiply(-2, 4) == -8


def test_safe_divide():
    assert safe_divide(10, 2) == 5
    assert safe_divide(1, 3) == pytest.approx(1 / 3, rel=1e-6)


def test_safe_divide_zero():
    with pytest.raises(ValueError):
        safe_divide(1, 0)
