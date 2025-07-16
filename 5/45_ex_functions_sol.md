# Exercise - Functions revisited

- Recall that functions are defined with `def`.
- They can take zero or more paramters as input
- They do something.
- They have a `return` or output.
- Remember, you can recursively keep calling the same function, (though you may blow out a stack if you go too deep)

## Build the following functions

1. Build a function that prints hello then a name. (use an f-string)
    "hello, mike" or something as output

```python
def hey_you(n):
    return f'Hello, {name}'
```

2. Build a function that computes the perimeter of a square given a side

```python
def p_square(x):
    return 4 * x
```

3. Build a function that takes the perimeter of a polygon of n-sides

```python
def p_poly(l):
    return sum(l)

def p_poly2(*args):
    return sum(args)
```

4. Build a function that takes a list and adds the word 'hello' in between each letter

```python
def why_is_this_an_exercise(l):
    return 'hello'.join(l)
```

5. Build a function that computes the nth fibonacci number
1,2,3,5,8,13...  (make sure you start by testing with small numbers)

```python
def fib(x):
    if x <= 1 :
        return x
    else:
        return fib(x-2) + fib(x-1)
```

6. If you couldn't do large numbers add a list outside of already computer fib numbers to make this much faster

```python
def fib_w_cache(x):
    cache = {}
    def fib(x):
        if x <= 1 :
            return x
        elif x in cache:
            return cache[x]
        else:
            res = fib(x-2) + fib(x-1)
            cache[x] = res
            return res
    return fib(x)
```