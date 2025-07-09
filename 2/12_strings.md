# Strings

In python strings are defined with single or double quotes.  Either is pefrectly fine and equivalent.

```python
s = 'abc'
t = "123"
```

The reasons you might select one over the other is:

- a style guide dictates you use one.
- you have a special character in your string.

```python
s = 'Don't forget'. # This is wrong and breaks
s = "Don't forget"  # This is fine.
s = "He gave a stern "No"" # This is wrong and breaks
s = 'He gave a stern "No"' # this is fine.
```

But what about when we need to use special characters?

| Escape Sequence | Meaning                   | Example                                     |
| --------------- | ------------------------- | ------------------------------------------- |
| `\\`            | Backslash                 | `"C:\\\\Users\\\\Name"` → `C:\Users\Name`   |
| `\'`            | Single quote              | `'It\\'s fine'` → `It's fine`               |
| `\"`            | Double quote              | `"He said: \\\"Hi!\\\""` → `He said: "Hi!"` |
| `\n`            | Newline                   | `"Hello\\nWorld"` →<br>`Hello`<br>`World`   |
| `\t`            | Tab                       | `"Hello\\tWorld"` → `Hello    World`        |
| `\r`            | Carriage return           | `"Hello\\rWorld"`                           |
| `\b`            | Backspace                 | `"abc\\b"` → `ab`                           |
| `\0`            | Null character            | `"abc\0def"`                                |

If we had to use a single quote in a single quoted string, the right way would be...

```python
s = 'Don\'t forget!'
```

We'll also commonly use this for newlines and tabs

```python
s = 'one\n\ttwo\n\t\tthree'
```

will render:

```
one
    two
        three
```

## string functions
strings are very common in programming.  As such, we have a number of built in functions that we can use

```python
>>> s = 'Hello, World!'
>>> print(s.lower(), s.upper())
hello, world! HELLO, WORLD!
>>> 
>>> print('o', s.count('o'))
o 2
>>> 
>>> print('h', s.count('h'))
h 0
>>> print(s.count('l'), s.count('ll'))
3 1
```

## Comparing strings
We can compare strings with == operator.  

```python
>>> a = 'hello'
>>> 'hello' == a
True
>>> 'l' in a
True
>>> 'hello ' == a
False
>>> 
```

Notice, whitespace will result in strings not matching.  we can fix this with `strip()`

```python
>>> 'hello '.strip()
'hello'
```

Also there's `lstrip()` and `rstrip()` for just one side of the string

## Splitting and joining
Sometimes we want to split strings into parts.  Separating on spaces or something else.  (when we get to csvs this is essential)

```python
>>> s = 'Hello, World from Mike!'
>>> s.split()
['Hello,', 'World', 'from', 'Mike!']
>>> s.split('o')
['Hell', ', W', 'rld fr', 'm Mike!']
>>> s.split('l')
['He', '', 'o, Wor', 'd from Mike!']
>>> t = s.split('r')
>>> t
['Hello, Wo', 'ld f', 'om Mike!']
>>> 'r'.join(t)
'Hello, World from Mike!'
>>> '|'.join('abcdefg')
'a|b|c|d|e|f|g'
>>> '|'.join(['abcdefg'])
'abcdefg'
>>> ''.join([1,2,3,4])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: sequence item 0: expected str instance, int found
>>> ''.join([str(x) for x in [1,2,3,4]])
'1234'
>>> 
```

We'll get into list comprehension later.

## Large and multi-line strings

if we have a really big string (normally we should load this from a file) we can use """ or ''' (both equivalent) to define the string

for example:

```python
>>> s = """ this is
... my really large
... string with a number
... or newlines in it
... """
>>> s
' this is\nmy really large\nstring with a number\nor newlines in it\n'
>>> 
```

