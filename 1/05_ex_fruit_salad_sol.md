# Exercise - Fruit Salad

1. Create a list of at lease 8 fruits.  The fruits should be strings
2. add 'mango' to the list of fruits
3. Get the length of the list.
4. check if "tomato" is in fruits
5. check if "apple" is in fruits
6. create a set called pico, add "tomato" and "pepper" to it.
7. check if anything in pico is in fruits
8. remove anything in pico from fruits


```python
>>> fruits = ['apple', 'banana', 'cherry', 'date', 'eggplant', 'grape', 'lemon', 'orange']
>>> fruits += ['mango']
>>> fruits
['apple', 'banana', 'cherry', 'date', 'eggplant', 'grape', 'lemon', 'orange', 'mango']
>>> len(fruits)
9
>>> 'tomato' in fruits
False
>>> 'apple' in fruits
True
>>> pico = {'tomato', 'pepper'}
>>> any(pico) in fruits
False
>>> pico.intersection(fruits)
set()
>>> fruits += ['tomato']
>>> pico.intersection(fruits)
{'tomato'}
>>> fruits.remove('tomato')
>>> fruits
['apple', 'banana', 'cherry', 'date', 'eggplant', 'grape', 'lemon', 'orange', 'mango']
>>> 
```
