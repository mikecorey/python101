# Files

Python can interact with files a number of different ways.  It includes libraries to read csv (comma separated values), json (javascript object notation), xml, pickle, config, zip, etc.

Direct file management gives our programs persistence so we can write off data and read it later.  Also we can accept inputs from files and process them.

We'll start with just standard file handling.

## Opening and Closing files.
In Python, we open files with a built-in function, `open(filename, mode)` which returns a file handle (a variable representing a file)

the function accepts a `filename` which is relative to the location in which the script is being run.

Additionally, it accepts a `mode` as a string.  The mode is how we'll be accessing the file.

- `'r'` read (error if file does not exist)
- `'w'` write (creates if does not exist)
- `'rb'` reads the file in binary mode (no encoding processing)
- `'a'` append (opens for writing (to end) or creates new file if does not exist)
- `'x'` exclusive create (creates a new file, errors if the file exists)
- `'wb'` writes in binary mode (you write bytes not strings)


If we open a file, we MUST close it.  Closing is simple.  Just use `f.close()` .  Failing to close a file results in bad things happening:
- The file could stay locked
- Other processes can't touch the file
- We hold an OS resource (the file descriptor)
- Data might not be written!
- Weird bugs

Example, say we want to read the text file `moby_dick.txt`.  We can open and close it like this... 

```python
f = open('moby_dick.txt', 'r')
s = f.readline()    # reads a line from the file
f.close()
```

(either pull moby dick from project gutenberg or it's in ../assets)


## `with` keyword,
If closing files is so essential, how do we guarantee we do it?  The common way is to use `with`.  When using `with` we tell python to execute this codeblock with a variable defined, when the code block exits for any reason automatically call `.close()`,

So we can reduce our original code to
```python
with open('moby_dick.txt', 'r') as f:
    f.readline()
do_something_else()
```

This is much neater, we can now use f for the entire scope of the code block within `with`.  When it's done, close happens automatically.

## writing files
We can write files using mode `'w'`.  in this we just send a string in f.write().

```python
summary = input('Enter a comprehensive summary of moby dick: ')
with open('summary_of_the_whale.txt', 'w') as f:
  f.write(summary)
```

This example creates a file in the present directory named `summary_of_the_whale.txt`.  We then write a string to it.

A weird note about scope.  After `with` ends, f is closed but technically not gone.  We can still reference it.  Referencing a closed file is of limited utility.

## A note on file names
**NEVER EVER EVER UNDER ANY CIRCUMSTANCE LET A USER NAME A FILE IN AN UNTRUSTED SETTING**

```python
fn = input('enter a filename to write ')
with open(fn, 'w')
    ...
```

Why? because an untrusted user could go ahead and write to `/etc/` or something critical (there's some assumptions there about privledges but the concern is real)

if you must. always provide a base dir which is safe to write to and sanitize out any special characters that may modify path.

That's not to say you can't programmatically write files, but just be careful.

## How to read

Say we've opened our text file with open().  We now have a few options to read a file.

- `.read()` This will read the entire file into memory.  For larger files, this could be a bad idea.  Plus, often we want to just work with smaller chunks.

```python
>>> f = open('../assets/moby_dick.txt', 'r')
>>> s = f.read()
>>> len(s)
1238226
>>> 
```

- `.read(n)` This reads n bytes from the file (less standard in text mode)
```python
>>> f = open('../assets/moby_dick.txt', 'r')
>>> f.read(10)
'\ufeffThe Proje'
>>> f.read(10)
'ct Gutenbe'
>>> f.read(10)
'rg eBook o'
>>> f.read(10)
'f Moby Dic'
>>>
```

- `.readline()` - reads a line up to a newline character
```python
>>> f = open('../assets/moby_dick.txt', 'r')
>>> f.readline()
'\ufeffThe Project Gutenberg eBook of Moby Dick; Or, The Whale\n'
>>> f.close()
```

- `.readlines()` - reads the entire text into memory but stores each line as it's own string in a list.  This is popular for iterating over every line.

```python
>>> f = open('../assets/moby_dick.txt', 'r')
>>> l = f.readlines()
>>> l[0]
'\ufeffThe Project Gutenberg eBook of Moby Dick; Or, The Whale\n'
>>> l[105]
'CHAPTER 33. The Specksnyder.\n'
>>> f.close()
```

- `.readline()` reads a single line from the input file.  This is so common that for can just iterate over f and it returns f.readline()

```python
with open('../assets/moby_dick.txt') as f:
    for line in f:
        do_something(line)
```

## Seek and tell
When reading files there's a cursor (like a position) that exists to show where we are in a file.  If we need to bounce around through a file (more common for binary stuff), we can use

- `.seek(n)` to jump to spot `n` (like 0 for start) which will let us jump to the beginning.

- `.tell()` returns the position of where the cursor is currently pointed.

## writing
Writing to files is done with the `.write` or `.writelines()` methods.  It should be noted we must provide our own newlines.  The key difference between the two.

-`write()` expects a string and will write it to a file

-`writelines()` will write a list to a file.  You provide the `\n` still for each line.


