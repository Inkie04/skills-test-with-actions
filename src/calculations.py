import pytest
from src.calculations import area_of_circle, get_nth_fibonacci

# ---------- area_of_circle ----------

def test_area_of_circle_positive():
    assert area_of_circle(2) == pytest.approx(12.566, rel=1e-3)

def test_area_of_circle_zero():
    assert area_of_circle(0) == 0

def test_area_of_circle_negative():
    with pytest.raises(ValueError):
        area_of_circle(-1)


# ---------- fibonacci ----------

def test_fibonacci_zero():
    assert get_nth_fibonacci(0) == 0

def test_fibonacci_one():
    assert get_nth_fibonacci(1) == 1

def test_fibonacci_normal():
    assert get_nth_fibonacci(6) == 8

def test_fibonacci_negative():
    with pytest.raises(ValueError):
        get_nth_fibonacci(-5)