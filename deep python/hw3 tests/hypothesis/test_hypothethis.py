import string
import random
from hypothesis import given, settings, HealthCheck
from hypothesis import strategies as st
import pytest

from hypothethis import generate_unique_strings


def test_check_realization():
    # тест проверяет что у вас что-то получилось
    result = generate_unique_strings(100)

    assert len(result) ==100
    assert sorted(set(result)) == sorted(result)


@given(st.integers(min_value=1, max_value=1000))
@settings(suppress_health_check=[HealthCheck.too_slow])
def test_generate_unique_strings(n):
    result = generate_unique_strings(n)
    # допишите тут тест и напишите новые кейсы :-)
    assert len(result) == len(set(result)), "Список содержит дубликаты"



@given(st.integers(min_value=1, max_value=1000))
@settings(suppress_health_check=[HealthCheck.too_slow])
def test_string_len_and_symbols(n):
    result = generate_unique_strings(n)
    for i in result:
        assert 5 <= len(i) <= 10, f"Неверная длина строки, надо было от 5 до 10 включительно, а не {len(i), i}"
        for x in i:
            assert (ord(x) in range(48,58)) or (ord(x) in range(65,91)) or (ord(x) in range(97,123)), f"Некорректный символ, ожидаютя только латинские буквы + цифры, а {x} не то, не другое"


@given(st.integers(min_value=1, max_value=1000))
@settings(suppress_health_check=[HealthCheck.too_slow])
def test_incorrect_answer_len(n):
    result = generate_unique_strings(n)
    assert len(result) == n, f"Ответ длины {len(result)}, а надо {n}"
