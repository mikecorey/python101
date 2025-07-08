# Arithmetic Operators
Python supports common math operations.

| Operator | Meaning    | Example |
| -------- | ---------- | ------- |
| `+`  | add | `2 + 3` → `5`   |
| `-`  | subtract | `5 - 2` → `3`   |
| `*`  | multiply | `4 * 3` → `12`  |
| `/`  | float division | `7 / 2` → `3.5` |
| `//` | floor divition | `7 // 2` → `3`  |
| `%`  | modulus / remainder | `7 % 2` → `1`   |
| `**` | exponent | `2 ** 3` → `8`  |

```python
>>> a = 3 
>>> a * 100
300
>>> 9 / a
3.0
>>> 9 // a
3
>>> 5 % 2
1
```

# Parentheses
You can use parentheses just like you'd use in normal math.  You can also add them just to make code more legible or if you want to ensure execution order.

```python
>>> (3 + 4) * 5
35
>>> 3 + (4 * 5)
23
```

# Bitwise Operators
| Operator    | Symbol | Example  | Meaning                         |
| ----------- | ------ | -------- | ------------------------------- |
| AND         | `&`    | `a & b`  | 1 if **both** bits are 1        |
| OR          | `\|`   | `a \| b` | 1 if **either** bit is 1        |
| XOR         | `^`    | `a ^ b`  | 1 if bits are **different**     |
| NOT         | `~`    | `~a`     | Inverts all bits                |
| Left Shift  | `<<`   | `a << n` | Shift bits **left** `n` places  |
| Right Shift | `>>`   | `a >> n` | Shift bits **right** `n` places |

```python
>>> a = 16
>>> a >> 1
8
>>> a << 1
32
```

Remember in these, we're not assigning anything to `a` just doing the operation.

If you want to do that, many operators have an augmented assignment operator counterpart.

```python
>>> a = 16
>>> a += 8
>>> a
24
```

Please ensure your code is legible if you do this though.  Personal preference, but `**=`, `//=`, `<<=` are confusing to read.

# functions
I want to quickly touch on functions.  While we can certainly just put operations in the REPL and do basic arithmetic.  functions make code repeatable and reusable.

You've already seen a function `hello()`.  It took zero arguments and just returned "Hello, world".

For right now, i just want to show that we can put code in a function to make it usable.

```python
>>> def add_two(x):
...     return x + 2
... 
>>> add_two(5)
7
>>> add_two(-1)
1
>>> add_two('car')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in add_two
TypeError: can only concatenate str (not "int") to str
>>> 
```
functions can take multiple parameters.  They're just separated by commas.

```python
>>> def add_together(x,y):
...     return x + y
... 
>>> add_together(2,3)
5
>>> add_together(-3,3)
0
>>> add_together('car', 'boat')
'carboat'
>>>
```

above is an example of duck typing.  (If it looks like a duck and it quacks like a duck). You should be able to see the benefits and drawbacks.
