class Coordinates:
  
  def __init__(self):
    print("Constructor")
  
  def __init__(self, first, second):
    self.x = first
    self.y = second
  
  def __str__(self):
    return str(self.x)

  def distance(self, other):
    return str(self.x - self.y)



myCoord = Coordinates(3, 4)
print(myCoord)

otherC = Coordinates(0, 0)
print(myCoord.distance(otherC))




class Animal:
  
  def __init__(self, name):
    self.name = name
  
  def greeting(self):
    print(self.name)

class Dog(Animal):

  def __init__(self):
    super(Dog, self).__init__(self)


one = Animal("potato")
one.greeting()