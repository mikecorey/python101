# Collections

Python has three main collection types, lists, tuples, and sets.
- Lists are an ordered sequence which can contain duplicates
- Tuples are ordered, unchangable, and can have duplicates
- Sets are unordered, changeable, with no duplicates

## Why?
These are incredibly useful when building programs.  We don't need repeated variables names etc. we just reference the collection instead.

```python
>>> polygon_side_1 = 4
>>> polygon_side_2 = 2
>>> polygon_side_3 = 1
>>> polygon_side_4 = 8
>>> polygon_perimeter = polygon_side_1 + polygon_side_2 + polygon_side_3 + polygon_side_4
>>> polygon_perimeter
15
>>> polygon_sides = [4,2,1,8]
>>> polygon_perimeter = sum(polygon_sides)
>>> polygon_perimeter
15
```

# Lists
- An ordered, mutable (changeable), sequence.
- We define these with square brackets `[]` and put commas in between values.
- `[1,2,3,4]` the list containing 1,2,3 and 4 in that order.
- we can access an individual element of the list with `[n]`.
```python
>>> a = ['car', 'boat', 'train', 'bike']
>>> a[1]
'boat'
```
WAIT?! Why wasn't the result `'car'`?
  - Lists are zero-offset in python meaning that a[n] means the `n` elements after the first.

(Technically lists are different than an array (not a contiguous block of memory, more an object / next_ptr style.)  I'll likely screw up and call the lists arrays somewhat regularly.
  - numpy does have arrays, we'll get to those much later.

Really neat: We can access from the end of the list using a negative offset.

```python
>>> a[-1]
'bike'
```

## Length
We get the length of a list with `len(a)`

```python
>>> len(a)
4
```

## Slices
To get a portion of a sequence (list, tuple, str) we can use a slice.

```python
>>> a[2:3]
['train']
```
Note that its from the 2 offset not including the 3 offset.

If we want to get really crazy, there's actually a 3rd part to a slice where we specify the step size.
- so if we wanted every other item we could call

```python
>>> a[::2]
['car', 'train']
>>> a[1::2]
['boat', 'bike'] 
```

- More practical, we can specify negative step to reverse the list.

```python
>>> a[::-1]
['bike', 'train', 'boat', 'car']
```

Again, please consider readability when doing this.  Maybe put in a comment.

## Setting items in lists
Lists are mutable.  (i.e. they can be changed.)

We can simply update lists with assignment by offset.

```python 
>>> a = [1,2,3,4]
>>> a[2] = 6
>>> a
[1, 2, 6, 4]
```

# Checking if an item is in a list
<<TODO>>


# Sets
A set is an unordered collection which able to be changed.  It cannot contain duplicates.

Sets are defined with set() or {}.

```python
>>> a = set([1,2,3])
>>> a
{1, 2, 3}
>>> a = set()
>>> a
set()
>>> a = {1,2,3}
>>> a
{1, 2, 3}
>>> type(a)
<class 'set'>
```

So naturally you can define an empty set with: 
```python
>>> a = {}
>>> type(a)
<class 'dict'>
>>> 
```

WRONG! using `{}` will create an empty DICTIONARY (we'll get to those later)

For now, be careful to define sets with `set()`.

Really useful for finding unique elements in a list.

```python
>>> a = [1,2,3,4,3,2,3,4,3,2,1,2,2,2,2,1,1,1,2,2,2,3,3,2,1,2,3]
>>> set(a)
{1, 2, 3, 4}
```

## Adding elements
We can add elements with `.add()`

```python
>>> c = set([1,3,5])
>>> c
{1, 3, 5}
>>> c.add(2)
>>> c
{1, 2, 3, 5}
```

Note: `.add` is actually modifying the set, not adding an element to the output but keeping the list intact.

## Removing elements
We can remove an element with `.remove`.  If the element doesn't exist, a KeyError is thrown.

```python
>>> c.remove(3)
>>> c
{1, 2, 5}
>>> c.remove(99)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 99
```

## Set operations
We can do standard operations on sets unions, intersections, differences.

```python
>>> c = {1,2,3}
>>> d = {2,3,4,5}
>>> c.union(d)
{1, 2, 3, 4, 5}
>>> c.intersection(d)
{2, 3}
>>> c.difference(d)
{1}
>>> d.difference(c)
{4, 5}
```

# Tuples
Tuples are a collection which is ordered, immutable and can have duplicates.  This is somewhat similar to lists excapt they cannot be changed.

## Defining a tuple

We define a tuple with `()` or we can use `tuple(l)` where `l` is a list.

```python
>>> p = (4,1,-2)
>>> p
(4, 1, -2)
```

## Limited Operations
Because they're immutable, there's really only a couple things we do with tuples.

we can `.count(x)` the number of times `x` is in a tuple.  Additionally, we can `.index(x)` to see where x occurs in the tuple.

## When to use tuples
In practice you'll almost never use `.count()` or `.index()`.  Tuples are common because we can do multiple assignment

```python
>>> def divide_and_remainder(x, y):
...     return x // y, x % y
... 
>>> result = divide_and_remainder(9, 4)
>>> quotient, remainder = divide_and_remainder(9,4)
>>> result
(2, 1)
>>> quotient
2
>>> remainder
1
```

Also you do multiple assignment directly as you set variables, but it's somewhat unreadable...

```python
>>> a,b = 1,2
>>> a
1
>>> b
2
```

## Technically you can mix types
All the examples I've shown so far have been of the same type in a list.

However, you can technically mix multiple types in the same list, set or tuple.  

While this makes sense for tuple, I can't think of a good reason to do that with lists.

```python
>>> a = [1, 'one', 1.0]
>>> a
[1, 'one', 1.0]
```
