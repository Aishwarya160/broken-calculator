from calculator import add, multiply

def test_add():
    result = add(2, 3)
    if result != 5:
        raise AssertionError(f"Expected add(2, 3) to return 5, but got {result}")

def test_multiply():
    assert multiply(3, 4) == 12 

# fix the add function in the calculator module
# calculator.py
def add(x, y):
    return x + y 

def multiply(x, y):
    return x * y