# Errors

Errors happen when something unexpected happens in your program.  Some common examples are:

- SyntaxError you typed something in your code wrong.

- ValueError something is wrong with a value

- TypeError a function can't manipulate the type of a variable you provided

- IndexError you tried to reference something outside of the bounds of your sequence

- KeyError you searched for a key that wasn't there.

- FileNotFoundError you tried to open a file that didn't exist.

All of these are specializations of the general class Error.

When an error happens, if your program doesn't have a way to `handle` it, it will stop executing.

This is not ideal in most cases.  I've had programs that ran for an afternoon then come back to find an error and progress was lost.  Ideally, we want to handle these and move on with the next operation.

## Handling errors

We handle errors with try/except blocks.  (These are similar to try catch in other languages)

In try except blocks we acknowledge that an operation may fail and `try` it.  So if we're opening a file we might do:

```python
try:
    f = open('zzz.txt', 'r') # a file that doesn't exist
    f.readline()
except FileNotFoundError as e:
    print('got a file not found error!')
```

This will catch a FileNotFoundError and handle it.

These errors are classes which are children of Error.

For example FileNotFoundError has all the methods and attributes below:

```
>>> f = FileNotFoundError()
>>> f.
f.add_note(           f.errno               f.strerror
f.args                f.filename            f.with_traceback(
f.characters_written  f.filename2           
```

We can use these to describe our error to the user, but often, just a print will do.  These are primarily for debugging.

## Multiple errors

We don't have to have just one except block.  We can have multiple to catch multiple types of errors and handle them differently.

```python
try:
    f = open("data.txt", "r")
    content = f.read()
    
except FileNotFoundError:
    print("not found.")
except PermissionError:
    print("bad permissions.")
```

## Excepting everything
Technically you could simply just try and excapt everything.  This may seem like a good idea.  But if something failed in a module you called, you program will handle the exception and you'll never know why.  Plus it will handle everything the same way.  This is not ideal.

Best practice is to avoid catching any error as it will lead to unexpected results.

But, here's how it's done...

```python
try:
    do_something_that_might_fail()
except:
    print('something happened.')
```


## `else` we can also run a block of code if the try block DID NOT fail...

```python
try:
    do_something()
except:
    print('uh oh')
else:
    print('phew everything worked')
```

## `finally`
Finally, we can use finally which will execute no matter if an error happened or not.  For example, you might put file.close() here if you didn't use `with`... but you should have used `with`.

```python
try:
    do_something()
except:
    print('uh oh')
else:
    print('phew everything worked')
finally:
    print('the scary part is over.  continuing with less risky code')
```

## Raising your own exceptions
If you want a function to return an error if something breaks, (a user provided a bad value, etc).  We can use `raise`.  Raise allows us to emit an error from our function, terminate execution of the function and let the caller function do something with it.

We can even provide a description.

```python
>>> def do_a_thing(x):
...     if x != 'run':
...             raise ValueError('you were supposed to send run.')
...     print(f'hey we are going to do {x}')
... 
>>> do_a_thing('jump')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in do_a_thing
ValueError: you were supposed to send run.
>>> do_a_thing('run')
hey we are going to do run
>>> 
```


## Custom Exceptions
You could technically make your own error class.  Just make a class that implements Exception.  Most of the time though, the built-ins are good enough.

