# Exercise - Functions Default variables


1. Write a function called subract_two_nums.  The user must supply two numbers, but if they only supply one, assume the second is zero.

```python
>>> def subtract_two_nums(x: int, y: int = 0):
...     return x - y
... 
>>> subtract_two_nums(4)
4
>>> subtract_two_nums(4,3)
1
>>> 
```

2. Write a function called join two lists.  The user must provide one list, but the second is optional.  Write this with type hints

```python
>>> from typing import Any
>>> def join_lists(l1: List[Any], l2: List[Any] = None):
...     l2 = l2 or []
...     return l1 + l2
... 
>>> join_lists([1,2,3], [4,5,6])
[1, 2, 3, 4, 5, 6]
>>> join_lists([1,2,3])
[1, 2, 3]
>>> join_lists([4,5,6])
[4, 5, 6]
>>> 
```

3. Write a function called my_info.  You must provide a name, however addr, phone, city, state, zip are optional however the default value for state is FL.  Print all the info provided.

```python
>>> def my_info(name, addr=None, phone=None, city=None, state='FL', zip=None):
...     city = city or ''
...     print(f'Name: {name}\nAddr:{addr}')
...     print(f'{city}, {state}  {zip}')
...     print(phone)
... 
>>> my_info('mike', '123 Elm St', zip=32566)
Name: mike
Addr:123 Elm St
, FL  32566
None
>>> 
```

4. write a function called join_four_strings.  all strings are optional.  return them joined.

```python
>>> def join_four(s1=None, s2=None, s3=None, s4=None):
...     s1 = s1 or ''
...     s2 = s2 or ''
...     s3 = s3 or ''
...     s4 = s4 or ''
...     return s1 + s2 + s3 + s4
... 
>>> join_four('a', 'bc', 'de', 'fgh')
'abcdefgh'
>>> 
```

5. write a function called fav_things which takes a str name and a list of favorite things (all strings) and prints them.
    - create favorite things for two people

```python
>>> def fav_things(name: str, things: List[Any]=None):
...     things = things or []
...     print(f'{name}\'s favorite things are:')
...     for t in things:
...             print(f'\t{t}')
... 
>>> fav_things('bill', ['🍖', '🌏', '❄️'])
bill's favorite things are:
	🍖
	🌏
	❄️
>>> fav_things('john', ['🐶', '🏒'])
john's favorite things are:
	🐶
	🏒
>>> 
```