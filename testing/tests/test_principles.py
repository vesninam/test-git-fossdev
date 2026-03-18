import sys
# TODO make with `pip install -e .`
sys.path.append("../src")

from math_demo import (
    add,
    add_with_bug,
    add_something,
    calulcate_tax_with_bug,
    calulcate_tax
)

# [DONE] Ранее тестирование позволяет съэкономить время позднее
# [DONE] Тесты показывают наличие ошибок, а не отсутвие 
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
    #assert add_with_bug(5, 6) == 11 # WIll fail if uncommented
    print("Test BUG ADDITION PASSED")

def test_addition_duplicated_logic():
    # bad test since it relies on absence of `+` in add()
    assert add(6, 3) == 6 + 3 
    print("Test DUPLICATED LOGIC PASSED (could get some bugs in)")
    # good test since input and output are independent from add()
    assert add(6, 3) == 9 
    print("Test DUPLICATED LOGIC PASSED")

def test_addition_overcomplicated():
    # would work but slow and not actually needed 
    for i in range(0, 2**32):
        for j in range(0, 2**32):
            assert add(i, j) == i + j # bad since violates "duplication" 
            assert add(-i, j) == -i + j
            assert add(i, -j) == i - j
            assert add(-i, -j) == -i - j

def test_addition_resonable():
    assert add(6, 3) == 9 
    assert add(0, 3) == 3
    assert add(0, -3) == -3 
    assert add(-7, 83) == 76 
    assert add(-7, -83) == -90
    print("Test ADDITION with REASONABLE NUMBER of CASES PASSED ")


def test_add_something_reasonable():
    add_something(6, 3) == 9
    add_something(None, None) == 0
    add_something(None, "abc") == 0
    add_something(None, 10) == 0
    add_something("abc", 10) == "abc10"
    add_something(10, "abc") == "10abc" # what if operation is not commutative
    add_something("xyz", "abc") == "xyzabc"
    print("Test ANOTHER ADDITION with REASONABLE NUMBER of CASES PASSED ")

def test_tax_calculation():
    #using only integers doesn't allow test all cases
    assert calulcate_tax_with_bug(1000) == 150.
    assert calulcate_tax_with_bug(2000) == 300.
    assert calulcate_tax_with_bug(30) == 4.5
    assert calulcate_tax_with_bug(1) == .15
    #assert calulcate_tax_with_bug(1.7) == .25 will fail here

def test_tax_calculation_fight_pecticdes():
    #using only integers doesn't allow test all cases
    assert calulcate_tax(1000) == 150.
    assert calulcate_tax(2000) == 300.
    assert calulcate_tax(30) == 4.5
    assert calulcate_tax(1) == .15
    assert calulcate_tax(1.7) == .25
    print("Test TAX CALCULATION (FIGHT PECTICIDES)")
    
    
    print("Test TAX CALCULATION PASSED")

if __name__ == "__main__":
    test_addition_basic()
    test_bug_addition_notsufficient()
    test_addition_duplicated_logic()
    test_bug_addition_enough()
    test_add_something_reasonable()
    test_addition_resonable()
    test_tax_calculation()
    test_tax_calculation_fight_pecticdes()

    
