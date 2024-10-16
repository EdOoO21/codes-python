import pytest

from parse_duration import parse_duration
def test_some_convertions_without_floats():
    assert parse_duration("1293ns") == 1293
    assert parse_duration("211ms") == 211000000
    assert parse_duration("1us") == 1000
    assert parse_duration("0s") == 0
    assert parse_duration("8h23m") == 28800000000000 + 1380000000000

def test_some_convertions_with_floats():
    assert parse_duration("4.5m") == 270000000000
    assert parse_duration("-1.5h") == -5400000000000
    assert parse_duration("25.98h") == 93528000000000

def test_some_convertions_with_mixed_values():
    assert parse_duration("4h1223ms") == 14400000000000 + 1223000000
    assert parse_duration("8h23m") == 28800000000000 + 1380000000000

def test_invalid_time_type():
    with pytest.raises(ValueError):
        parse_duration("4x")

def test_invalid_time_value():
    with pytest.raises(ValueError):
        parse_duration("xx")

def test_no_time_value():
    with pytest.raises(ValueError):
        parse_duration("x")

def test_no_time_type():
    with pytest.raises(ValueError):
        parse_duration("123131")

def test_zero_subvalue():
    assert parse_duration("8h0m") == 28800000000000

def test_zero_mainvalue():
    assert parse_duration("0h4.5m") == 270000000000

def test_empty():
    with pytest.raises(ValueError):
        parse_duration("")

# def test_afew_subvalues():
#     assert parse_duration("-8h4.5m111s1223ms2323us") == - (28800000000000 + 270000000000 + 111000000000 + 1223000000 + 2323000)



