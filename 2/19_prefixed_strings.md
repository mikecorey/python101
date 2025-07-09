# Prefixed Strings

Python has a few types of special strings to shortcut formatting.

# f strings (format)

Python has format strings which allow you to provide inline variables and python operations.

This avoids concatenating strings.
```python
>>> print('the sum of two twos is ' + str(2+2) + ' unless you listen to radiohead')
the sum of two twos is 4 unless you listen to radiohead
>>> print('the sum of two twos is ', str(2+2), 'unless you listen to radiohead')
the sum of two twos is  4 unless you listen to radiohead
```

as you can see, this is confusing and we need to add spaces.

however, with f strings we can simply say...

```python
>>> print(f'the sum of two twos is {2+2} unless you listen to radiohead')
the sum of two twos is 4 unless you listen to radiohead
```

we can put any single line expression in curly braces to tell python to evaluate it and convert it to a string.

```python
>>> def reverse_string(s):
...     return s[::-1]
... 
>>> print(f'if hello looked in a mirror it would see {reverse_string('hello')}...')
if hello looked in a mirror it would see olleh...
```

# b strings (bytes)
byte strings are strings of raw bytes in python.  If we have binary data (like an image) we'd use a b string.  We can also use them for converting between character-sets.

# r strigs (regex)
Regexes are a special set of strings which let you match more elegantly than gigantic for loops etc which you saw earlier.  

for example, to match a dob, you could use the regex:
```python
r"\d{1,2}/\d{1,2}/\d{2}"
```

As you can see, regexes has a number of backslashes.  using an r string lets you avoid constant double `\\`