# Version 3.6.2

print("Hello World")

num = 5
print(num)

myStr = "My String"
print(myStr)
print("This is" + myStr)

print(6 + num)

print(str(num) + "666")




if(num < 10):
  print(num < 10)
elif(num > 9):
  print("^^^")
else:
  print("")

while False:
  print("Infinite loop")

while(num < 8):
  num += 1

myList = ["this", "something", "nothing", "everything"]

for element in range(5):
  print(element)

for element in myList:
  print(element)




# functions

def myFunction():
  print("Inside function")

myFunction()

def Caller(x):
  print(x + x)

Caller(-1)

def sum(first, second):
  return first + second

print(sum(15, 16))


