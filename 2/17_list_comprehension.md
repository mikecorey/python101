# List Comprehension
Sometimes it's not prudent to manually enter every value of a list in our code.

As such, we can build a list with a for loop.

```python
>>> my_list = []
>>> for i in range(10):
...     my_list += [i / 2]
... 
>>> print(my_list)
[0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5]
>>> 
```

Python gives us a simpler way to do this called dictionary comprehension.
In dictionary comprehension we can build the list in one line.

```python
>>> my_list = [x / 2 for x in range(10)]
>>> my_list
[0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5]
>>> 
```

This is strictly just a nicety and creates functionally equivalent objects to the example using a for loop.

We can also add if conditions to our list.

```python
>>> my_list = [x / 2 for x in range(10) if not 3 <= x <= 4]
>>> my_list
[0.0, 0.5, 1.0, 2.5, 3.0, 3.5, 4.0, 4.5]
```

Question: Why is 1.5 and 2.0 missing instead of 3.5?

We can have NESTED comprehensions too.

```python
>>> my_list = [x-1 for x in [x * 2 for x in range(10)]]
>>> my_list
[-1, 1, 3, 5, 7, 9, 11, 13, 15, 17]
>>> 
```

Be careful.  Legibility is RAPIDLY decreasing.


# Dictionary Comprehension
We can build dictionaries programmatically too.  Remember for a dictionary we could initialize it with

```python
>>> my_dict = {}
>>> for x in t:
...     my_dict[x[0]] = x[1]
... 
>>> my_dict
{'mike': 40, 'matt': 45, 'mark': 35}
>>> 
```

That absolutely works but it's a bit verbose.  Instead we can use dictionary comprehension.


```python
>>> t = [('mike', 40), ('matt', 45), ('mark', 35)] 
>>> my_dict = {k: v for k,v in t}
>>> my_dict
{'mike': 40, 'matt': 45, 'mark': 35}
>>> 
```

Note we define a dictionary item with `k:v`.  (those variables can be whatever you want) but they MUST be separated by a colon.  Otherwise you get a red herring `SyntaxError: did you forget parentheses around the comprehension target?`

## Does that `for k,v in t` work more generally?
YES! As long as you have a tuple coming out of your collection (or being generated) you can 100% unpack the tuple.

```python
>>> for k,v in t:
...     print(f'{k}😂{v}')
... 
mike😂40
matt😂45
mark😂35
>>> 
```

Bonus!  dict.items() is a method which will emit a tuple.

```python
>>> my_dict
{'matt': 45, 'mark': 35}
>>> for k,v in my_dict.items():
...     print(f'{k}😂{v}')
... 
matt😂45
mark😂35
```


# Set Comprehension
We can also construct sets by comprehension.  This is somewhat uncommon but a useful immediate use of this is for finding unique elements of some complex set.


```python
>>> s = {x // 2 for x in range(8)}
>>> s
{0, 1, 2, 3}
>>> type(s)
<class 'set'>
>>> student = ['bill', 'fred', 'fred', 'adam', 'mike']
>>> unique_students = {x for x in student}
>>> unique_students
{'mike', 'fred', 'bill', 'adam'}
>>> 
```

Of course we could also just construct the set with the list which will automatically do that step for us.




