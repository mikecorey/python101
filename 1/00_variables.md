# Variables

## Assignment

- A variable is just a name that holds a valuie.

- variables are assigned.

```python
>>> a = 3 
>>> b = 'MIKE'
>>> c = set()
>>> d = a
>>> a
3
>>> b
'MIKE'
>>> c
set()
>>> d
3
>>> 
```

- `a` is assigned the integer 3
- `b` is assigned the string `MIKE`
- `c` is assigned the result of `set()` (which creates a set)
- `d` is assigned the value of `a` (which is 3)

```python
>>> e = 3.0
>>> a == e
True
>>> f = '3'
>>> a == f
False
>>> 
```

- `e` is assigned the float value 3.0
- python will equate the integer 3 to the float 3.0
- python will NOT equate the string `3` to the integer 3
  - you can **cast** a string to an int if you want to do that comparison though.

```python
>>> int(f) = 3
  File "<stdin>", line 1
    int(f) = 3
    ^^^^^^
SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?
>>> int(f) == 3
True
>>> 
```

- Note that I screwed up equals and assignment in this block.  That'll be a gotcha that occurs regularly.
  - But it's better than c which will let you `a = 3` returns 3 so it evaluates to true! (yikes)

## Variables are case-sensitive
- `a` does not equal `A`.  Those are two separate variables.
- style dictates that capitals are normally for classes or constants. lowercase for variables functions etc.
- frankly all of python is case sensitive.  Even when comparing strings 'a' does NOT equal 'A'
  - to compare these normally you'd convert them to the same case.
  

## PEP Style Guide
There's an entire style guide for python if you want to be OCD about it.  Note: Your org may have it's own style guide which is different than PEP.

## Typing
- Python is **Dynamically** typed.
- Versus many other languages where i set a type and it stays that way through it's entire use. (static typing)

```python
>>> a = 3
>>> a = 4.0
>>> a = 'Car'
>>> a = set()
>>> 
```

## Naming
- Variables must start with a letter or underscore `_`, (cannot start with a number)

```python
>>> asd_123 = 'hello'
>>> asd_123
'hello'
>>> asdOneTwoThree = 'goodbye'
>>> asdOneTwoThree
'goodbye'
>>> 
```

## Naming styles
- `asd_123` is called **snake case**
- `asdOneTwoThree` is called **camel case**

### Underscores starting names
- technically variables can start with underscores `_`.  private things in a class will begin with `_` like `_my_internal_var`.  There's also `__my_very_hidden_var` this will actually be renamed (mangled) at runtime to avoid access outside of a class.  It means "seriously, don't touch this".


## Reserved Words
- Some words are reserved in a programming laguange for example, you cannot use `as` as a variable name.

```python
>>> as = 3
  File "<stdin>", line 1
    as = 3
    ^^
SyntaxError: invalid syntax
>>> 
```
- `as` is normally used in imports (ex:`import pandas as pd`)
- some others are `if`, `for`, `def`, etc.
- you can, but absolutely should not redefine function names

```python
>>> print = 4
>>> print('Hello, world')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not callable
>>> 
```

- True is a reserved word and value.  So it will throw a weird error.  Again, avoid using reserved words.

```python
>>> True = 3
  File "<stdin>", line 1
    True = 3
    ^^^^
SyntaxError: cannot assign to True
```

## Constants... sort of
In Python You'd denote a constant with ALL CAPS and underscores for spaces.`MAX_USERS`, `THREADS`, etc. However, this is in style only.  Python does not truly support constants so you could (BUT REALLY SHOULD NOT) overwrite those variables.

