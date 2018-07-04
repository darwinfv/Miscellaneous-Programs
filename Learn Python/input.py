
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.reverse()
fruits.append('grape')
fruits.sort()
fruits.pop()
print(fruits)



from collections import deque
queue = deque([1, 4, 17])
queue.append(31)
queue.popleft()
print(queue)


# dictionaries
import oop


for x in range(1, 11):
	print('{0:2d} {1:3d} {2:4d}'.format(x, x**2, x**3))


f = open("note.txt")
for line in f:
	print(line, end='')
# f.readline()


value = ('the answer', 42)
print(str(value))



for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()



def divide(x, y):
	try:
		result = x / y
	except ZeroDivisionError:
		print("divide by zero")
	else:
		print(result)
	finally:
		pass


prompt = "Type: "
pl = input(prompt)
print("You typed " + pl)