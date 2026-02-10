from script import add, divide

def test_addition():
    a = 3
    b = 4.5
    result = 7.5
    assert add(a, b) == result
    print("Test addition PASSED")

def test_division():
    a = 5
    b = 2
    result = 2.5
    assert divide(a, b) == result
    print("Test division PASSED")

def test_zero_division():
    a = 5
    b = 0
    try:
        divide(a, b)
        print("Test zero-division FAILED")
        assert False
    except ValueError as e:
        print("Test zero-division PASSED")

if __name__ == "__main__":
    test_addition()
    test_division()
    test_zero_division()
