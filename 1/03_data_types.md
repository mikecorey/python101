# More on Data Types

## None
`None` is a special value. It means nothing.  In C it'd be like `null`.  We can use this when testing to see if something has a value.

```python
>>> x = None
>>> x == None
True
>>> x is None
True
```
- x is assigned `None`
- you can do `x == None` or `x is None`.  Technically x is none is the standard.

## Types
We can get the type of a variable with the function `type(x)`

```python
>>> type(a)
<class 'int'>
>>> type(b)
<class 'str'>
>>> type(c)
<class 'set'>
```

None is of type NoneType

```python
>>> x = None
>>> type(x)
<class 'NoneType'>
```

## Casting
Many types can be cast (or converted) to other types.  As you saw in the last exercise, the strings you took from the user needed to be converted to integers or floats in order to have math done on them.

So for example, you can cast a string to an integer with `int(s)` where `s` is the string.

```python
>>> int('3')
3
```
we can also cast floating point numbers to integers.  This is useful to get the floor of a number.

```python
>>> int(3.14)
3
```

other functions for casting are:
- int() to integer
- float() to float
- str() to string
- bool() to boolean

There's a few more for complex types (like list()) but we'll cover those later.

## str()
- str() is universal.  You can cast everything to a string.  Maybe be a bit judicuous with it though.

```python
>>> str('asd')
'asd'
>>> str(3)
'3'
>>> str(None)
'None'
>>> str(True)
'True'
>>> str(ValueError)
"<class 'ValueError'>"
>>> 
```


## Boolean?
A quick note on boolean values.  I don't find this particularly intuitive.  I would avoid using this if possible for ints.

```python
>>> bool(0)
False
>>> bool(1)
True
>>> bool(2)
True
>>> bool(-1)
True
>>> bool('True')
True
>>> 
```

## Errors when casting
There's obvious exceptions where casting won't work.  For example, you can't cast `a` to a number.  this results in a `ValueError` being thrown.

```python
>>> a = 'a'
>>> int(a)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'a'
```

## What about that 'with base 10' part?
You can actually specify the base as a second parameter for int.  For example

```python
>>> int('1111', 2)
15
```

but if you do it with an int, it fails:

```python
>>> int(1111, 2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: int() can't convert non-string with explicit base
```

## Type Checking
If you need to check a type, you can use `isinstance(x, t)` to do this.  (Where x is the variable and t is the type you're checking) This will return a boolean (T/F) of whether the types match

```python
>>> isinstance('a', str)
True
>>> isinstance(_, bool)
True
>>> 
```

