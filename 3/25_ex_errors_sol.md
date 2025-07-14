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

```python
d = {'a': 1, 'b': 2}

def get_val(s):
  try:
    return d[s]
  except KeyError:
    print('fyi, c isn\'t in there')
    return None

print(get_val('a'))
print(get_val('c'))
```

4. Read a file and count the lines.  Handle the filenotfounderror and if the file has zero lines Divide by zero error.

```python

with open('empty_file.txt', 'w') as f:
  pass



def read_a_maybe_empty_file(fn):
  try:
    with open(fn) as f:
      tot_chars = 0
      num_lines = 0
      for l in f:
        tot_chars += len(l)
        num_lines += 1
      return tot_chars / num_lines
  except FileNotFoundError:
    print('no file')
    return 0
  except ZeroDivisionError:
    print('no lines')
    return 0


print(read_a_maybe_empty_file('not_empty_file.txt'))
print(read_a_maybe_empty_file('empty_file.txt'))
print(read_a_maybe_empty_file('zzz.txt'))
```