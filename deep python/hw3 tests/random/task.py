import random
import mock
from mock import patch

def patch_random(x: int):
    """
    Функция которая должна патчить в исполнении randint
    """
    return min([111, 222, 333, 444, 555, 666, 777, 888, 999], key=lambda n: abs(n - x))


def broken_random() -> int:
    """
    Генерация случайного числа с использованием patch, который корректирует нечеткие числа.
    """
    original_random =random.randint
    with patch('random.randint', side_effect=patch_random):
        return patch_random(original_random(100, 1000))

