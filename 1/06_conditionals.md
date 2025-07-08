# Conditionals
Up until this point, our programs really haven't been interesting.  This is because flow was static and everything was just executed in a list.

Conditionals allow branching in the program.  This allows us to check if a specific condition is true and execute on branch if so.  Or we can execute a branch if it's falso, Or we can check more conditions.

## `if` / then
In python the basic branch is done via `if`.  The syntax is:

```python
if condition:
    do_something()
```

do_something will only be performed if the condition is true.  Anything indented after the if will be considered in the same code block.  But what if we want to do one thing or another but not both?

A bad approach would be checking the condition then checking the negation of the condition. 

```python
if condition:
    do_something()
if not condtion:
    do_the_other_thing()
```

Instead we have `else` this is much easier to read and much more logical for complex conditions.

```python
if condition:
    do_something()
else:
    do_the_other_thing()
```

In this case we will only execute one or the other.  furthermore if checking the condition takes awhile we aboid doing it twice.

If we want to check a bunch of things we can use `elif`.

```python
if condition:
    do_something()
elif another_condition:
    do_something_else()
elif a_third_condition:
    do_another_thing()
else:
    do_the_other_thing()
```

This is useful when we have a set of things we want to check, but only execute one of them.  If none of the checks pass, we then can `do_the_other_thing()` as a base case.

## comparison operators

The following operators can be used to compare values for a condition.  They return `True` or `False`.

| Operator | Meaning               | Example  |
| -------- | --------------------- | -------- |
| `==`     | Equals                | `x == 5` |
| `!=`     | Not equal             | `x != 5` |
| `<`      | Less than             | `x < 5`  |
| `>`      | Greater than          | `x > 5`  |
| `<=`     | Less than or equal    | `x <= 5` |
| `>=`     | Greater than or equal | `x >= 5` |

## boolean operators
Additionally, we can combine conditions with `and`, `or`, `not`.

`P and Q` evaluates to `True` if and only if `P` and `Q` are both `True`.

`P or Q` evaluates to `False` only if `P` and `Q` are `False`.

`not P` simply inverts the truth value of `P`.  If `P` is `True`, `not P` is `False` and vice-versa.


## Truthy and Falsy
For readability, it's best that the condition evaluates to `True`, `False` or maybe `None`.  Python will evaluate other values to either `True` or `False` based on their truthy or falsy values.

Things that eval to false:
- `0`
- `0.0`
- `None`
- `''`
- `[]`
- `{}`

You could more specifically say `a is None` or `b == 0` or `len(c) == 0`.  So try to avoid things that are equal to false.

## Membership and Identity
we can check if a value is in a collection using `in`.  For example

```python
>>> a = [2,4,6,8]
>>> 3 in a
False
>>> 4 in a
True
```

Be careful, we cannot use this for sets of things being in a collection.

We can check if a value is the same object.  This is not all that common, Normally we're just checking if something `is None`.  This is done by

```python
if a is not None:
    print('a is set')
```

But there's a few cases where we want to check if objects are the same.  Beware this is somethat confusing:

```python
>>> a = []
>>> b = []
>>> c = a
>>> a == b
True
>>> a is b
False
>>> a is c 
True 
```

`a == b` because `a` and `b` are both empty lists
`a is b` is false though because `a` is not the exact same object as `b`.  (Like not in the same memory location)
`a` is `c` is `True` because `c` was literally set to the same object.

## `any()` and `all()`
These check to see if any value in a list is truthy or if all values in the list are truthy.

```python
>>> a = ['', '', 'a', '']
>>> any(a)
True
>>> all(a)
False
```


