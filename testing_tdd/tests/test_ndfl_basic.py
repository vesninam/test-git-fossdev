from ndfl import calculate_tax

def test_basic_ndfl():
    assert calculate_tax(200_000) == 26_000