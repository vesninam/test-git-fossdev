def add(a, b):
    return a + b


def add_with_bug(a, b):
    return a * b

def add_something(a, b):
    if a is None or b is None:
        return 0
    if isinstance(a, str) or isinstance(b, str):
        return str(a) + str(b)
    return a + b

def calulcate_tax_with_bug(income):
    return income * 0.15

def calulcate_tax(income):
    return int(income * 0.15 * 100) / 100.
