# Exercise 1

Given two sides of a right triangle, compute the hypotenuse

```python
a = input("Enter side A: ")
b = input("Enter side B: ")
a = int(a)
b = int(b)
c = ((a ** 2) + (b ** 2)) ** (1/2)
print('The hyp is', c)
```

```
💣 mikecorey 1 👉 python pyth.py
Enter side A: 8
Enter side B: 15
The hyp is 17.0
```


# Exercise 2

Given a radius find the area of a circle.

```python
r = input("Enter radius: ")
r = float(r)
PI = 3.14159
a = PI * r ** 2
print('The area is', a)
```

```
💣 mikecorey 1 👉 python area_of_circle.py 
Enter radius: 2
The area is 12.56636
💣 mikecorey 1 👉 python area_of_circle.py
Enter radius: 10
The area is 314.159
```

