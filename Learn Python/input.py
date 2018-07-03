
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



















prompt = "Type: "
pl = input(prompt)
print("You typed " + pl)