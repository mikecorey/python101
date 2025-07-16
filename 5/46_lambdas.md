# Lambdas

lambdas are one liner functions. they're very useful for quick sorting, filtering and tiny functions that we'll apply to our code.

the format is:

```python
lambda arguments: expression
```

they take zero or more arguments.

here's a very basic example:

```python
add = lambda x, y: x + y
print(add(2, 3))
```

This is the same as 
```python
def add(x, y):
    return x + y
```

In case you're wondering here's what a zero arg function would look like

`f = lambda :2+3`

unless theres an global variable or something we need to access and modify with is function, this is a bit weird.


# Where you see these

## sorted()
Say i have a list of tuples and i want to sort them based on the 2nd value.  I can do this with lambdas


```python
pairs = [(1, 3), (2, 2), (4, 1)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
```

## map()
What if i wanted to square a bunch of numbers in a list?

```python
nums = [1, 2, 3]
squared = list(map(lambda x: x**2, nums))
```

## Filters

What if i wanted to define a filter...

```python
nums = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, nums))
```

## Best practices.
- Keep lambdas small.
- If there's much more going on than something you can quickly look at and read, it's probably best to use a regular function
- Debugging is a bit more complicated with lambdas (hard to dive into the lambda)

