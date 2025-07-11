# Packages, Modules, Imports

So far we've been working primarily in one file (or notbebook).

But we should at least be aware of how python packages and associates bigger projects.

# Modules
In python a module is just a single `.py` file.  We use code from these using `import mymod` or `from mymod import f`.

# Packages
Packages are bigger collections of associated files.  We know something is a package because it has an `__init__.py` file in its directory.  This file could even be blank.

if we access a package we'll often use `import mypack.mymod` or `from mypack.mymod import f`.

# Imports

As mentioned the first day, python has modules for almost everything.  It's even an xkcd joke.  [antigravity](https://xkcd.com/353/)

Again, be careful what you're importing because some stuff could be sketchy.

We can get packages from pip (the standard package installation tool.)

From a command line we could install a package just by calling 

```
pip install requests
```

This will go check for a package named requests and install it.

In a jupyter notebook (or colab) we can run this command in a code cell prefixing it with `!`.

```
!pip install requests
```

The notebook will go out and retrieve the lalstet version of the package from pypi.

# Exercise
In a notebook install and import python requests.

run requests.get('http://google.com') and get the text response from it.

# Common packages you'll use...

`sys` contains system commands.  

- `sys.argv` the command used to run the program
  - doesn't apply in notebooks

  - the filename is always sys.argv[0]

- `exit()` exits the program.
  - not sure what happens in notebook

  - you can provide a status code

- `path` where python will look for modules

- `stdin` and out and err.  Will pull

`random` functions that generate random data

- `random` generates a float between 0 and 1

- `randint` generates an int within a range

- `choice` takes a list and returns a random element of it

`os` operating system type functions

- `listdir` lists files in dir

- `mkdir` creates a folder

- `mkdirs` makes nested directories

- `path` module with a bunch of path methods

- `os.path.exists` check if a file exists

- `rename` renames a file

`math` common math things

- `PI` a constant representing pi

- `sin` sine of a number

- `sqrt` square root

Others we'll talk about in detail:

`re` regular expressions

`json` json

`datetime` dates and time


# import `as`

Often, it's not efficient to use an entire import name for a package you'll be using constantly.  For examlpe if I import

`import mikes_really_long_name_for_a_package`

that's inefficient.  because every time i need to use something within the package I'll have to write out:

```python
mikes_really_long_name_for_a_package.do_something()
mikes_really_long_name_for_a_package.do_something_else()
...
```

Instead we can use `as`.

In the case of `as`, we create an alias for a package name.  For example if we import:

```python
import mikes_really_long_name_for_a_package as mp

mp.do_something()
mp.do_something_else()

```

This is much more efficient to type and creates much shorter lines of code.

## common packages using `as`

Here's a few examlples of shortened packages you'll see in others code...

`import pandas as pd`

`import numpy as np`

`import matplotlib.pyplot as plt`

`import tensorflow as tf`

...

## What's in a module?

You can run help(module_name) to get a fantastic description of whats in modules.  It's very helpful and explains what each function does.  External modules may not be as good, but the built-ins are well documented.

For example, running `help(os)` will give you an interactive help dialog

```
Help on module os:

NAME
    os - OS routines for NT or Posix depending on what system we're on.

MODULE REFERENCE
    https://docs.python.org/3.12/library/os.html

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This exports:
      - all functions from posix or nt, e.g. unlink, stat, etc.
      - os.path is either posixpath or ntpath
      - os.name is either 'posix' or 'nt'
      - os.curdir is a string representing the current directory (always '.')
      - os.pardir is a string representing the parent directory (always '..')
      - os.sep is the (or a most common) pathname separator ('/' or '\\')
      - os.extsep is the extension separator (always '.')
:
```
