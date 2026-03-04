import sys
# TODO make with `pip install -e .`
sys.path.append("../src")

from math_demo import (
    add,
    add_with_bug
)

# Ранее тестирование позволяет съэкономить время позднее
# Тесты показывают наличие ошибок, а не отсутвие 
# Тесты не должны дублировать логику тестируемого кода
# Тесты не должны использовать ВСЕ наборы входных параметров
# Тесты должны покрывать "кластеры" входных параметров
# Тесты должны обнаруживать новые ошибки (pescicide paradox)
# Тесты покрывают как успешные так и ошибочные кейсы

def test_addition_basic():
    assert add(2, 2) == 4, "Function didn't returned 4"
    print("Test BASIC ADDITION PASSED")

def test_bug_addition_notsufficient():
    assert add_with_bug(2, 2) == 4, "Function didn't returned 4"
    print("Test BUG ADDITION PASSED")

def test_bug_addition_enough():
    assert add_with_bug(2, 2) == 4, "Function didn't returned 4"
    assert add_with_bug(0, 0) == 0
    assert add_with_bug(5, 6) == 11
    print("Test BUG ADDITION PASSED")


if __name__ == "__main__":
    test_addition_basic()
    test_bug_addition_notsufficient()
    test_bug_addition_enough()
