# Dictionaries

Sometimes searching lists or sets in python isn't ideal.  For example, say we wanted to get the age of a person.  To do this with lists and tuples we'd need to do one of the following.

```python
>>> ages = [('mike', 40), ('matt', 45), ('mark', 35)]
>>> def get_age(name):
...     for a in ages:
...             if a[0] == name:
...                     return a[1]
...     return None
... 
>>> get_age('mike')
40
>>> get_age('bill')
>>> 
```

Alternatively you could have two separate lists one for names and one for ages.  As long as they're sorted exactly the same, the function work.

```python
names = ['mike', 'matt', 'mark']
ages = [40, 45, 35]
```

again, what if the lists get out of sync. searching is O(n) time (not fast).

This is where dictionaries are useful.  Dictionaries are a set of key / value pairs.
- A key is a unique object which is searchable (like a string)
- A value is the object referenced by that key.

Think of this like an actual dictionary, look up a word (key) get a definition (value)

```python
>>> ages = {'mike': 40, 'matt': 45, 'mark': 35}
>>> ages
{'mike': 40, 'matt': 45, 'mark': 35}
>>> ages['mike']
40
```

using the syntax above we can get a key's value by referencing it within square brackets.

```python
>>> ages['matt']
45
```

if a key isn't found it raises a KeyError.

```python
>>> ages['bill']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'bill'
```

if we want to avoid KeyErrors we can either check if a key is in the dict or get and return a default value if the key is not found.

```python
>>> 'bill' in ages
False
>>> 'mike' in ages
True
>>> ages.get('mike')
40
>>> ages.get('bill', 999)
999
```

Soemtimes we want to iterate over all the items in a dict.  In this case, we can simply use a for loop.

```python
>>> for k in ages:
...     print(k)
... 
mike
matt
mark
>>>
```

Note: you can also specifically say you want to iterate over dict.keys but that's redundant.

## removing an item
Sometimes you want to remove an item from a dict.  Unfortunately this looks a bit weird in python.  We do it using `del`.  Note: we're not using parentheses.  It's a specific part of the syntax. Think of it as a keyword not a function.

```python
>>> del ages['mike']
>>> ages
{'matt': 45, 'mark': 35}
>>>
```

## complex types in dicts.
Dicts don't have to be simple keys and values.  While the key must be hashable (able to be decomposed into a searchable).  The value can be anything even another dict.

>>> people = {'mike': {'age': 40, 'car': 'sentra', 'zip': 32542}}
>>> people['mike']['age']
40
>>> people['mike']['car']
'sentra'
>>> 

Dictionaries are very powerful ways to store and lookup data.



