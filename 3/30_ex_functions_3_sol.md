# Exercise args


1. Create a function that joins together the strings provided by the user as input as args.  Do not take a fixed number of string.

```python
def joiner(*args):
  s = ''
  for a in args:
    s += str(a)
  return s

def joiner_oneline(*args):
  return ''.join([str(a) for a in args])

print(joiner(1,2,'asd'))
print(joiner_oneline(1,2,'asd'))
joiner(1,2,'asd',print)
```


2. Create a function that joins **four** strings.  This time, do NOT use four input variables but rather let the user provide them.  If they provide more, you only care about the first four.

```python
def joiner(*args):
  s = ''
  for a in args[:4]:
    s += str(a)
  return s

joiner(1,2,'asd',print,map,zip,'def',4,5,6)
```

3. Create a function that takes an unbound number of arguments. for each argument, if it's a string join it to the other strings, if it's a number add it to the other numbers

```python
def fancy_joiner(*args):
  s = ''
  tot = 0
  for a in args:
    if isinstance(a, str):
      s += a
    elif isinstance(a, float) or isinstance(a, int):
      tot += a
    else:
      print(f'not sure what to do with {type(a)} of the value {a}')
  print('the full string was', s)
  print('the total was', tot)

fancy_joiner(1,2,'abc',print,3,map,zip,'def',4,5,6, 'ghi', 'jkl', 7,8,9,0)

assert sum(range(10)) == 45
```

# kwargs

4. create a function that takes a number of keyword arguments.  For each keyword argument, if the key starts with 'r' print it.  Otherwise ignore it.

```python
def printr(**kwargs):
  for k in kwargs:
    if k.startswith('r'):
      print(k, kwargs[k])

printr(rad=4, rubble='asd', raspberry='hello', array=33, roundhouse='kick')
```

5. make a function that MUST have a keyword argument 'rate' in it.  If the argument is not supplied the program should print "rate missing".

```python
def required_rate(rate, **kwargs):
  print(rate)
  print(len(kwargs))

required_rate(33, hello=44)

def required_rate(**kwargs):
  if 'rate' in kwargs:
    print(kwargs['rate'])
  else:
    print('rate missing')

#thats an error
#required_rate(44, a = 'hello')


def required_rate(rate, *args, **kwargs):
  print(rate)
  print(len(args))
  print(len(kwargs))


required_rate(33,44,55,hello=44)
```

6. write a function that takes a number of positional and keyword arguments.  For each argument print it, for each keyword argument print the key and the value.

```python
def all_the_args(*args, **kwargs):
  print(args)
  print(kwargs)

all_the_args(4,3,2,a=55, b=66, c=77)
```
