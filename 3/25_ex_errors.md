# Exercise - Errors

1. Write a function that reads a file, but catches a file not found error

```python
def read_a_file(fn):
    f = None
    try:
        f = open(fn, 'r')
    except FileNotFoundError as e:
        print(f"couldn't open {fn}")
    finally:
        if f:
            f.close()
```
2. write a function `divide_all(l: List[int], x: int)`.  Catch an error if the user tries to divide by zero.

```python
def divide_all(l: List[int], x: int):
    res = None
    try:
        res = [z / x for z in l]
    except ZeroDivisionError:
        print('cant div by zero')
    return res
```

3. Write a block of code that searches a dict and catches a KeyError.


4. Read a file and count the lines.  Handle the filenotfounderror and if the file has zero lines Divide by zero error.
