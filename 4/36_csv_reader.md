
# `csv`

- a CSV library for python which streamlines reading and writing of comma separated value files.
---

## Overview `csv`

- `csv` ships with Python.  You do not need to pip install anything.
- Handles files in a streaming fashion (like readline (without the s)) 
- Can handle other delimeters besides just commas

Remember, reading CSVs without this package is very simple.

```python
with open('people.csv', 'r') as f:
    for l in f:
        row = l.split(',')
```

This doesn't handle fancy things like quoting, but it gets the job done 95% of the time.

The `csv` module streamlines the code somewhat with the added bonus of handling some additional cases.


Here's a very simple reader using csv...

```python
import csv

with open('people.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

And a very simple writer...

```python
with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'age'])
    writer.writerows([['Mike', 40], ['Matt', 45]])
```

In both cases we're essentially trading the `.split` or `.join` calls for `csv.reader(f)` or `csv.writer(f)`.  Code ends up looking a bit cleaner

## Reading CSV files

```python
with open('people.csv', newline='') as f:
    reader = csv.reader(f)
    header = next(reader)
    data = [row for row in reader]
```

- default delimeter is ','.
- bonus: we can put strings in double quotes `"` to protect against commas in strings etc.
- header reads the first line off the csv to a list.  (think of it like pop)
- we can read each rot using comprehension.
  - just remember this loads the entire file to memory.
- `newline=""` tells python to use the system settings for newline.  this will help avoid extra empty lines when processing.
 lets the module handle platform‑specific line endings.  
- values come off as strings.  you need to cast.  (but if you know the column heading...)

### `DictReader`

```python
with open("people.csv", newline="") as f:
    reader = csv.DictReader(f)
    for record in reader:
        print(record["name"], int(record["age"]))
```

- pulls the key names from the header.
- you still need to cast though.
- if you need to greatly rearrange the csv then this might have an advantage.

### Custom Delimiters & Quoting

```python
with open('data.tsv', newline='') as f:
    reader = csv.reader(
        f, delimiter='\t',]
        quoting=csv.QUOTE_NONE, 
        escapechar='\')
```

- `.tsv` is a common extension for tab-separated values.
- `quoting=csv.QUOTE_NONE` tells the csv reader to not look for quotes
- `escapehcar='\'` instead we use an escape char which each special character (\n and \t) must use to avoid incorrect reads


## Writing CSV Files

### Basic Writer

```python
rows = [('id', 'temp'), (1, 97.5), (2, 83)]
with open('temps.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)
```

- writes the header: id, temp
- writes 2 rows in one batch.  (calling `.writerows()`)

### `DictWriter`

Just like reader we can also write dicts to a csv.

```python
fieldnames = ['id', 'temp']
with open('temps.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'id': 1, 'temp': 97.5})
```

This seems somewhat inefficient, but if we already have our information in a dict, this might make sense.  We just set the ordering in `.writerow()`

### Dialects

Dialects allows us to sepcify a config that we can reuse,  so if we had a bunch of Pipe delimited files which were quotable we could do this...

```python
class PipeDialect(csv.Dialect):
    delimiter = '|'
    quoting   = csv.QUOTE_MINIMAL
    quotechar = '"'
    lineterminator = '\n'

csv.register_dialect('pipes', PipeDialect)

with open('pipe.psv', 'w', newline='') as f:
    writer = csv.writer(f, dialect='pipes')
    writer.writerow(["A", "B|C"])   # quotes second cell automatically
```

- If we have a common format or if we need to reuse our config across many files, this might make sense.
- We can also use `.sniffer` to guess the delimiters.  This should be avoided.

