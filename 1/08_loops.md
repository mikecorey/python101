# Loops

Python has two types of loops, `while` and `for`.  While checks a condition.  For does something for each element in an iterable.


## while loops

While will execute the same block of code repeatedly until the test condition is `False`.  In the same, if the condition is `False` at the start, it will never begin execution of any code.

The syntax for a while loop is
```python
while condition:
    do_something()
```

for example let's print out each character of a string until we hit a 't'.

```python
>>> s = "I ran to the store to buy milk."
>>> i = 0
>>> while s[i] != 't':
...     print(s[i])
...     i += 1
... 
I
 
r
a
n
 
>>> 
```

Python does not support a `do/while` loop.  Those are helpful for repeating something until a condition is met.  so if we wanted to check if a user enters 'x', then continue we'd need to intialize the value then enter the loop.

```python
>>> input_char = '\0'
>>> while input_char != 'x':
...     input_char = input('type x (then enter) to continue: ')
... 
type x (then enter) to continue: n
type x (then enter) to continue: n
type x (then enter) to continue: c
type x (then enter) to continue: x
>>> 
```

## for loops
The first example of iterating over something while a condition is met is not ideal.  For instance, if we forget to put the counter in the loop will run endlessly.

For loops solve this problem by iterating over a sequence.  For example, if we wanted to print every character in a string...

```python
>>> for c in 'OneTwo':
...     print(c)
... 
O
n
e
T
w
o
>>> 
```

That's much cleaner.  If we had a list, it's the same deal:

```python
>>> for s in ['one', 'two', 'three']:
...     print(s)
... 
one
two
three
>>> 
```

In C we'd have an initialization, condition, and increment.  Python doesn't have this because we iterate over a sequence.  So instead we have `range()`.

`range(stop)` will generate a sequence of values from 0 to `stop`.

```python
>>> for i in range(3):
...     print(i)
... 
0
1
2
>>>
```

You'll use range with just stop 99% of the time.

`range(start, stop)` will generate a sequence of values from `start` to `stop`.

```python
>>> for i in range(3,6):
...     print(i)
... 
3
4
5
>>> 
```

This is less common but in certain cases makes sense.  Alternatively you could just offset the number consider the first example, but `print(i+3)`.

`range(start, stop, step)` is slightly more common.  This will allow you to iterate from `start` to `stop` by an increment of `step`


```python
>>> for i in range(0,10,2):
...     print(i)
... 
0
2
4
6
8
>>> 
```

Note again, in all these cases, `stop` is not included in the loop.

## A note on "generate".

Python does not create the full list in memory of every value in the sequence then iterate over it.  Instead it generates the list on the fly.  This is very ideal because if the list is enormous or if it takes awhile to generate each element, the step would be very compute or memory intensive.

So if we look at `range()` more closely:

```python
>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

range actually `yields` the next number.  We won't dive into this in too much detail, but know that it's NOT creating the whole list for now.


## `break` and `continue`
sometimes we want to not do a full loop or quit early.

break and continue allows this.

`break` will terminate the entire loop and continue after the for.  it's like our condition has not been met suddenly and we drop out.

`continue` says we're done processing that one section and does the next iteration

```python
>>> for i in range(20):
...     if i % 2 == 0:
...             continue
...     if i > 10:
...             break
...     print(i)
... 
1
3
5
7
9
>>> 
```