
# Regex In Python

## Overview

Regular Expressions are a means of advanced string parsing.

We've seen before the difficulty of doing in-depth parsing and how quickly the code can begin to grow.

Regular expressions provide a simple means of checking text for format all in one line.

Note: Regular expressions are standardized and available across virtually all programming languages.

We simply import regex with:

```python
import re
```

## What do we want to do?

`re` has a few methods to handle common string functions `search`, `match`, `findall`, `sub`.

### `re.search()` – find **first** match

```python
text = 'my email is not mike123@example.com'

match = re.search(r'\w+@\w+\.\w+', text)    #We'll get into what this string means in a second.
print(match.group())  # mike123@example.com
```

### `re.findall()` – find **all** matches

```python
emails = re.findall(r'\w+@\w+\.\w+', "hi a@b.com c@d.com")
print(emails)  # ['a@b.com', 'c@d.com']
```

### `re.sub()` – replace matches

```python
text = re.sub(r'\d+', 'XXX', "Call 123-456-7890")  # 'Call XXX-XXX-XXX'
```

## Pattern Building Blocks

| Pattern      | Matches                          |
|--------------|----------------------------------|
| `.`          | Any character except newline     |
| `\w`         | Word char (letters, digits, _)   |
| `\d`         | Digit                            |
| `\s`         | Whitespace                       |
| `[...]`      | Character set                    |
| `[^...]`     | Negated character set            |
| `a|b`        | `a` or `b`                       |
| `^`, `$`     | Start, end of string             |
| `[a-zA-Z]`   | Just a letter not a number caps or lower |
| `(?=...)`    | Look ahead i.e. the following string must contain... but don't match it yet |

## Quantifiers & Groups

### Repeats

| Pattern   | Meaning                     |
|-----------|-----------------------------|
| `*`       | 0 or more                   |
| `+`       | 1 or more                   |
| `?`       | 0 or 1                      |
| `{n}`     | Exactly n                   |
| `{n,}`    | n or more                   |
| `{n,m}`   | Between n and m             |

```python
re.findall(r'a{2,4}', "caaabaaa")  # ['aaa', 'aa']
```

### Groups

We can use parentheses for groups.

```python
match = re.search(r'(\w+)@(\w+)\.(\w+)', "mike123@example.com")
print(match.group(1))  # mike123
print(match.group(2))  # example
print(match.group(3))  # com
```


## Flags & Compilation
Flags let us slightly modify our regex.  This makes for simpler patterns.

### Flags

```python
re.search(r'hello', 'HELLO', re.IGNORECASE)
re.search(r'^start', 'multi\nstart', re.MULTILINE)
```

(We could also bitwise or to do both.)

### Compile once, use a bunch

Ideally, we'd compile the pattern first.  Outside our search function.  Then we'd find matches within the function.  If speed is imperative this is the correct approach.

```python
email_pattern = re.compile(r'\w+@\w+\.\w+')

def check_email(s):
    email_pattern.findall(s)

check_email("x@y.com a@b.org")
```

## Also

Regular expressions are HARD! They're not intuitive at first.  As such, it's fine to go ahead and check your text on things like regex pal.  They'll help you get your regex tuned perfectly.