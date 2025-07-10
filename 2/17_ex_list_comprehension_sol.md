# Exercises - List Comprehension

1. Use list comprehension to create a list of even numbers (up to 30).  Do this two different ways!

```python
>>> [x for x in range(30) if x % 2 == 0]
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
>>> [x*2 for x in range(15)]
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
>>> 
```

2. Create a function that takes a list of strings.  Then using list comprehension return only the strings that start with 's'

```python
s = [s for s in 'she sells sea shells down by the sea shore'.split() if s.startswith('s')]
```

3. Create a function that checks if a string is digits.  If it is, create a total of digits and add to it.  (you can use sum() for this.)

```python
>>> i = ['123', '456', 'abcd', 'fgh', '789', '0', '-1']
>>> sum([float(x) for x in i if x.isdigit()])
1368.0
```

# Dictionary Comprehension
4. Create a dictionary containing the alphabet as keys and it's number as an offset (so a=1, b=2, etc.)

```python
>>> {chr(64+i): i for i in range(1,27)}
{'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
```

5. create a dictionary containing the alphabet and nubmer relations as above, but only keep letters with even values.
{b=2, d=4, f=6...}

```python
>>> {chr(64+i): i for i in range(1,27) if i % 2 == 0}
{'B': 2, 'D': 4, 'F': 6, 'H': 8, 'J': 10, 'L': 12, 'N': 14, 'P': 16, 'R': 18, 'T': 20, 'V': 22, 'X': 24, 'Z': 26}
```

# Set Comprehension

6. Create a function which takes a list of strings containing duplicates.  For every string, if it starts with an 'm' it can stay in the set.  If it does not, leave it out of the set.

[mike, matt, bill, mark, fred, fred, mark, bill, aaron] becomes {'mike', 'matt', 'mark'}


```python
>>> candidate_list = ['mike', 'matt', 'bill', 'mark', 'fred', 'fred', 'mark', 'bill', 'aaron']
>>> {x for x in candidate_list if x.startswith('m')}
{'mark', 'mike', 'matt'}
```

