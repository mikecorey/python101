# Exercise - testing

1. **DO NOT WRITE THE ACTUAL FUNCTION YET** You've been asked to write a function that takes two strings from a user and divides them.  The result is then converted back to a string and returned to the user.  Call it str_div.  Write the tests you need as a bunch of asserts.

2. Write the function and test it.

2. Convert them to unittest

Colab will be a bit weird, but you can run tests with...

```python
unittest.TextTestRunner().run(unittest.defaultTestLoader.loadTestsFromTestCase(TestStrDiv))
```

(assuming TestStrDiv is your test class)

3. Convert them to pytest

you can actually do this in bash within a notebook cell.

`!pip install pytest`

Then 

`!pytest test_str_div.py`

