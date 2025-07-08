# Exercise - FizzBuzz

(This is on leetcode.com as problem 412)

Fizz Buzz is a very popular interview question for programmers.  I don't know why.

Given an integer n, return a list of strings 1-indexed where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.

answer[i] == "Fizz" if i is divisible by 3.

answer[i] == "Buzz" if i is divisible by 5.

answer[i] == i as a string.

for example if n == 4 the output would be:

"['1', '2', 'Fizz', '4']"

```python
>>> n = 4
>>> answer = []
>>> for i in range(n):
...     x = i + 1
...     if x % 3 == 0 and x % 5 == 0:
...             answer += ['FizzBuzz']
...     elif x % 3 == 0:
...             answer += ['Fizz']
...     elif x % 5 == 0:
...             answer += ['Buzz']
...     else:
...             answer += str(x)
... 
>>> answer
['1', '2', 'Fizz', '4']
```

