# Exercise - Functions

## Type Hints

1. write a function that will join two strings called str_join make sure to add type hints for the parameters and return

```python
>>> def str_join(s1: str, s2: str) -> str:
...     return s1 + s2
... 
>>> str_join('cats', 'dogs')
'catsdogs'
>>> 
```

2. write a function that will join a string to a float to an int.  Call this function str_smash.  It will return a string.  use type hints


```python
>>> def str_smash(s: str, i: int, f: float) -> str:
...     return s + str(i) + str(f)
... 
>>> str_smash('hello', 5, 6.12)
'hello56.12'
```

3. write a function that will accept a float or an int and a float or an int.  Then it will sum them together and return a string in the format "the answer is x" where x is the result.  Use type hints.

```python
>>> from typing import Union
>>> 
>>> def wordy_sum(x: Union[int, float], y: Union[int, float]) -> str:
...     return f'the answer is {x+y}'
... 
>>> wordy_sum(3.14, 2)
'the answer is 5.140000000000001'
```

4. write a function that takes a list of strings and joins them.  call this str_combine.  Again, it returns a string and uses type hints.

```python
>>> from typing import List
>>>
>>> def str_combine(list_of_strings: List[str]) -> str:
...     s = ""
...     for l in list_of_strings:
...             s += l
...     return s
... 
>>> a = ['hello', 'mike', 'car', 'boat']
>>> str_combine(a)
'hellomikecarboat'
>>> 
```

5. write a function that takes a list of a bunch of things and joins them (any type really is fine.)  Return type is a string.

```python
>>> def str_combine(list_of_things: List) -> str:
...     s = ""
...     for l in list_of_things:
...             s += str(l)
...     return s
... 
>>> a = [print, 'asd', 3.14, -200, sorted]
>>> str_combine(a)
'<built-in function print>asd3.14-200<built-in function sorted>'
>>> 
```

could use List[Any]
