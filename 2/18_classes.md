# Classes

Classes are our first step into object-oriented programming.  For now we'll just be looking at the basics.

Think of classes as 'types of things' not tiny little data types but rather bigger classes of things.

person could be a class, car could be a class, DatabaseConnector could even be a class.

instances (or objects) are specific instants of a class.  So YOU are a person, my very awesome and economical sentra is an instance of car.  my_oracle_db_conn is an instance of DatabaseConnector.

we define classes with the `class` keyword.  Here's the simplest class.  It creates a class Dog

```python
>>> class Dog:
...     pass
... 
>>>
```

We can now create an instance of class.

```python
>>> titus = Dog()
>>> type(titus)
<class '__main__.Dog'>
```

titus (a bichon frise) is an instance of Dog.  That is to say he is a dog.  In fact **sigh** he's my dog.

You can see that the type is `__main__`.  This is simply because we generated dog in just a generic repl outside of a file.  It's not part of a module or something in which case it would have the modules name instead of `__main__`.

## isinstance
so far our class is very boring.  All we can really do is see if our instance (or anything) is an instance of Dog.

```python
>>> isinstance(titus, Dog)
True
```

## Properties or attributes
Ok well let's modify our class so it's a bit more useful.  We can add properties.  Properties are just variables that exist in every class, but in this case they are applied to this specifc instance.

So let's give our Dog class a name, and an age, maybe a color.

```python
>>> class Dog:
...     def __init__(self, name, age, color):
...             self.name = name
...             self.age = age
...             self.color = color
...             self.cute = True
... 
>>> titus = Dog('titus', 2, 'white')
>>> 
>>> titus
<__main__.Dog object at 0x101a73800>
>>> titus.age
2
>>> titus.cute
True
```

So now we have some more details.  Now our Dog class has a function `__init__`.  This is called the constructor.  When an instance is created, this function runs.  In it, we provided 3 variables, name, age, color.

We can get the properties (or set them) by using `.` dot notation.  So `titus.age` gets the age property set for the instance titus of the class dog.

we also set a `.cute` (sorry) property.  Note that it wasn't in the constructor's input parameters, but we can still create it in the constructor.

## methods
ok our dog is cute.  But it's really just a data structure.  It's not able to do anything.  This is where methods come in.  In methods we run functions that modify or get data from our instance.  Let's add a bark method and a happy_birthday method.

```python
>>> class Dog:
...     def __init__(self, name, age, color):
...         self.name = name
...         self.age = age
...         self.color = color
...         self.cute = True
...     def bark(self, n):
...         for _ in range(n):
...             print(f'{self.name} says woof.')  
...     def happy_birthday(self):
...         self.age += 1
... 
>>> titus = Dog('titus', 2, 'white')
>>> titus.bark(2)
titus says woof.
titus says woof.
>>> titus.age
2
>>> titus.happy_birthday()
>>> titus.age
3
>>> 
```

`Dog.bark(n)` will make our dog bark `n` times.  In it we get the name from `self`. and add it to a format string.

`Dog.happy_birthday` will increment our dog's age.  again `self` is passed to the method in the class definition, but we dont add it when calling our method from an instance.

So what is `self`?  Self is baiscally the data structure that holds all the state and information of our class.  it's the instance itself of the class.

## staticmethod
On the other side of the coin.  Static methods are methods that apply across all instances, or more specifically are related to the class, but don't affect anything inside a specifc instance.  They don't take `self` as a parameter and are basically just classic functions with a dot in front.

consider if we add years_to_human_years...

```python
...     def happy_birthday(self):
...         self.age += 1
...     @staticmethod
...     def years_in_human_years(dog_age):
...         return dog_age * 7
... 
>>> titus = Dog('titus', 2, 'white')
>>> titus.bark(1)
titus says woof.
>>> titus.years_in_human_years(2)
14
>>> Dog.years_in_human_years(3)
21
>>> 
```

We can technically call this with our instance titus.  But it's not ideal.  In fact we can't actually access titus's age because that was in the `self` and we don't have access to self in static methods.

Ideally we'd just call it from the class `Dog.years_to_human_years(m)`.

