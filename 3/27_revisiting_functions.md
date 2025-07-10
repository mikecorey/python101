# Functions again

As you've seen, we can define functions using the def keyword

```python
def split_on_delimiter(s, delimiter):
    return s.split(delimiter)
```

# type hints
We mentioned python was dynamically typed. That is, we don't have to provide a type when we declare variables.  However, python allows us to define type hints so someone using our function can see what the function expects.  For example:

```python
>>> def add_nums(x: int,y: int):
...     return x + y
... 
>>> add_nums(2,3)
5
```

In this case we define a function called add nums and tell the interpreter we want two ints to be passed to it.

Unfortunately, in practice, python doesn't enforce this.  we can still send it a couple strings and it will happily concetenate them without a single bit of fuss.

```python
>>> add_nums('car', 'boat')
'carboat'
```

Furthermore, we can specify what the return type should be.  Again, this is NEVER enforced at runtime.

```python
>>> def add_nums(x: int,y: int) -> int:
...     return x+y
... 
>>> add_nums('car', 'boat')
'carboat'
>>> add_nums(2,3)
5
```

## finding incorrectly used type hints

The only way to solidly catch the errors is to use a code analysis tool like mypy to see if there's any issues.

```bash
(.venv) michaelcorey@Michaels-MacBook-Pro 3 % mypy type_hints.py
type_hints.py:6: error: Argument 1 to "add_nums" has incompatible type "str"; expected "int"  [arg-type]
type_hints.py:6: error: Argument 2 to "add_nums" has incompatible type "str"; expected "int"  [arg-type]
Found 2 errors in 1 file (checked 1 source file)
```

That's substantial effort and unless it's baked into your CI/CD pipeline, you'll probably not bother.

All that to say, Python really doesn't care all that much about types.  Duck typing was the decision and they're serious.

## if you must

If it's absolutely essential to enforce types, you can use an if statement and raise a TypeError.  This will stop execution if the error is not handled by the calling function.  We'll discuss errors more later.

```python
def add_nums_only_ints(x, y): # we could also add type hints if we wanted to.
    if not isinstance(x, int):
        raise TypeError(f'x should be an int, got {type(x)}')
    if not isinstance(y, int):
        raise TypeError(f'y should be an int, got {type(y)}')
    return x + y

z = add_nums_only_ints(2,3)
print(z)

z = add_nums_only_ints('car', 'boat')   #this raises an exception
print(z)
```

```python
Traceback (most recent call last):
  File "/Users/michaelcorey/workspace/python101/3/type_hints.py", line 20, in <module>
    z = add_nums_only_ints('car', 'boat')
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/michaelcorey/workspace/python101/3/type_hints.py", line 11, in add_nums_only_ints
    raise TypeError(f'x should be an int, got {type(x)}')
TypeError: x should be an int, got <class 'str'>`
```

That was a lot of work, but it gets worse.  When you call `add_nums_only_ints` you should really handle those errors with a try except block.  So we'd add

```python
try:
    z = add_nums_only_ints('car', 'boat')   #this raises an exception
    print(z)
except TypeError as e:
    print('bad types were sent!', e)
```

We'll dive into error handling more later, but this is a huge burden for now.


## multiple types for hints
Because type hints do help people understand our code before they use it in their application, they are somewhat helpful.  Just know that they're mostly documentation, less code.

Because of python's flexibility, we can tell users our function accepts multiple types.  We can use a Union type to tell python we'll accept floats or ints.

Union and all complex type hints are found in the package typing so you'll have to import typing.  specifically we want to just pull union so we'll use `from` (more on this later)

```python
from typing import Union
```

with Union imported we can now define `add_nums` as taking float or int.

```python
def add_nums(x: Union[int, float], y: Union[int, float]) -> float:
    ...
```

We can see this is getting a bit verbose, so again, decide if it's worth it to add these or take multiple types.

## Complex types in type hints
Sometimes we might want to take in a list or return a set or other complex type.  These are also in typing.  

```python
from typing import List, Set

def get_first_item(l: List) -> Set:
    return set([l[0]])

get_first_item([1,2,3,4]) # returns {1}
```

Again, these are totally optional but help with people implementing your code.


# docstrings
Type hints do help others use our code.  without needing to inspect all the code, we can easily tell someone what types to provide.  We can add additional comments to help the user understand our function.  The primary comment for a function is called a docstring.  It is a multiline string which occurs right after the function's definition.

```python
def add_nums(x: int, y: int) -> int:
    """Add two numbers and return their sum.

    Args:
        x (int): The first number.
        y (int): The second number.

    Returns:
        int: The sum of the two numbers.
    """
    return x + y
```

This is actually pretty neat because that docstring gets associated with the function.  We can immediately call help(add_nums) and get the following output

```python
>>> help(add_nums)

Help on function add_nums in module __main__:

add_nums(x: int, y: int) -> int
    Add two numbers and return their sum.

    Args:
        x (int): The first number.
        y (int): The second number.

    Returns:
        int: The sum of the two numbers.
~
~
```

So it's our full docstring with type hints!  Again, if you're building a script for internal use, probably not necessary. but if you're building a larger system or contributing code to a large team.  That's pretty useful.  

These type hints and docstrings are used by IDEs like vscode to assist the user with understanding what paramters do what.


# functions with multiple variations
Because functions are just a name, we can't make multiple versions of the same function like we could in C.  Say a version that takes a single int and a version that takes a single string.  Python would just overwrite that first function.

For example:

```python
>>> def f(x):
...     print(x)
... 
>>> def f(x,y):
...     print(x,y)
... 
>>>
```

in this, we create f which takes one argument, then we create f that takes two argument.  when calling the function with one we get the error.

```python
>>> f(4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: f() missing 1 required positional argument: 'y'
```

This is because f that only takes one argument is gone. it was overwritten by the second.

So to get around this we have a number of options, the most common is default values.

```python
>>> def f(x, y=3):
...     print(x,y)
... 
>>> f(2)
2 3
```

we can specify default values for arguments.  this way we can say if a user doesn't specify a value, just use this one.  This is very helpful in writing functions.  A few notes on this

- Positional arguments must come before any keyword arguments.  In this case y is a keyword argument.

- just because it's a keyword doesn't mean it doesn't have a position.  We don't need to use y=3 if we call the function.  We can treat it as if it accepted 2 arguments.

```python
>>> f(2,4)
2 4
```

- We can still do type hints.  It's getting messier now though.

```python
>>> def f(x, y: int=3) -> None:
...     print(x,y)
... 
>>> f(5)
5 3
```

## args
Say we just wanted to take a bunch of positional args and we really don't care how many (that's how `print()` works.  just separate the things you want by commas and it prints them all.)

We can define our function with a `*` to tell python to just put all the arguments in a tuple.  then we can access that tuple however we want.  Commonly we'd iterate over them.

```python
>>> def f(*args):
...     for a in args:
...             print(f'😂{a}')
... 
>>> f(4,3,2,2,1)
😂4
😂3
😂2
😂2
😂1
```

Don't overdo it, because we're now making it a challenge to understand what our function takes as input.  This absolutely makes sense in many cases though.

One final note, technically `args` is a variable you named.  You could name it somethng else.  You never should do that.  It's agreed on that `args` is what you use when you do that.

## kwargs
What if we didn't have a set of positional arguments but rather we wanted to provide a list of key value pairs like the keyword arguments above.  To do this we can use a double asterisk.

```python
>>> def g(**kwargs):
...     for k,v in kwargs.items():
...             print(k,v)
... 
>>> g(a=3,b=4,c=5)
a 3
b 4
c 5
```

So now we're getting very messy, but you can actually use both args and kwargs in your function.  Be careful with this as we now have a ton of stuff going on in one function.

```python
>>> def f(*args, **kwargs):
...     for a in args:
...             print(a)
...     for k,v in kwargs.items():
...             print(k,v)
... 
>>> f(1,2,3,4,3,a='c')
1
2
3
4
3
a c
```

Note, you must still put kwargs after args (keyword after positional).

Also, yes you could call `kwargs` whatever you wanted.  But it's been decided that kwargs is what you should use.

