class Adder:
  def __init__(self, x):
    self.x = x
  
  def add_num(self, y):
    return y + self.x

  def add_permanent(self, y):
    self.x += y
    return y

a = Adder(3)
print(a.add_num(7))

print(a.x)

print(a.add_permanent(-2))

print(a.x)

print(a.add_num(4))