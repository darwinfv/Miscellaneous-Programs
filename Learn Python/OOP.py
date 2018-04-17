class Coordinates:
  
  def __init__(self):
    print("Constructor")
  
  def __init__(self, first, second):
    self.x = first
    self.y = second
  
  def __str__(sefl):
    return "yee"
  
  def distance(Self, other):
    return (self.x - other.x) ** 2



myCoord = Coordinates(3, 4)
print(myCoord)

otherC = Coordinates(0, 0)
print(myCoord.distance(otherC))




class Ani:
  
  def __inti__(self, name):
    self.name = name
  
  def greeting(self):
    print("YO")

class Dog(Animal):

  def __init__(self):
    super(Dog, self).__init__(self)


one = Animal
