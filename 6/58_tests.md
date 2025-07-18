# Python Testing

## Overview
We often want to test our code.  In fact, for production systems we SHOULD test all our code.  This is about not so much making sure you can code, but rather making sure our functions perform as expected.  Expecially when others add code to our codebase.

## `assert` the easy way

The built-in `assert` statement checks if an expression is `True`.

```python
def add(a, b):
    return a + b

assert add(2, 3) == 5
assert add(0, 0) == 0
assert add(-1, 1) == 0
```

If the assertion fails, Python raises an `AssertionError`.


## Writing Unit Tests with `unittest`

Python has a built-in test library called `unittest`.

```python
import unittest

def multiply(a, b):
    return a * b

class TestMathOps(unittest.TestCase):
    def test_multiply_positive(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_multiply_zero(self):
        self.assertEqual(multiply(0, 5), 0)

    def test_multiply_negative(self):
        self.assertEqual(multiply(-2, 3), -6)

if __name__ == '__main__':
    unittest.main()
```

Run the test file:
```bash
python test_file.py
```

Useful methods:
- `assertEqual(a, b)`
- `assertTrue(x)`
- `assertFalse(x)`
- `assertRaises(exception)`

## The external lib way, `pytest`

Install `pytest`:
```bash
pip install pytest
```

Write tests with plain `assert`:

```python
# test_math.py

def divide(a, b):
    return a / b

def test_divide_normal():
    assert divide(10, 2) == 5

def test_divide_zero():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
```

Before doing something like raises would require:

```python
def test_divide_zero():
    try:
        divide(5, 0)
        assert False
    except ZeroDivisionError:
        assert True
```

Run with:
```bash
pytest test_math.py
```

Pytest automatically:
- Finds functions starting with `test_`
- Displays helpful output on failure
- Supports fixtures and parameterized tests


## Best Practices

- Name test files like `test_*.py`
- Use `tests/` directory for organization
 (a little frustrating when testing things in other folders, but we can execute from root `python tests/test_multiply.py`)
- Use version control and automate test runs (e.g., GitLab Runners)
- Write tests before fixing bugs to lock them down
