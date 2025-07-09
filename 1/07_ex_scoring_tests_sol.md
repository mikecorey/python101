# Exercise - Scoring Tests
A student receives a grade for a test. The grade is assigned using the values below

90 - 100 = A

80 - 90 = B

70 - 80 = C

<70 = F


Given a grade provided from `input()` assign a letter grade.  Example `65` returns `F`.  `93` returns `A`.

```python
>>> score = int(input('enter score '))
enter score 96
>>> grade = 'F'
>>> if score >= 70:
...     grade = 'C'
... 
>>> if score >= 80:
...     grade = 'B'
... 
>>> if score >= 90:
...     grade = 'A'
... 
>>> grade
'A' 
```
