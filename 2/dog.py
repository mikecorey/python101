class Dog:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
        self.cute = True
    def bark(self, n):
        for _ in range(n):
            print(f'{self.name} says woof.')  
    def happy_birthday(self):
        self.age += 1
    @staticmethod
    def years_in_human_years(dog_age):
        return dog_age * 7
