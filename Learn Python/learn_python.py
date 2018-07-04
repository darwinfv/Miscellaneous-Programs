# is checks if two variables refer to the same object, but == checks
# if the objects pointed to have the same values.

# Equivalent of C's '?:' ternary operator
"yahoo!" if 3 > 2 else 2  # => "yahoo!"

li = []
li.append(1)    # li is now [1]
li.append(2)    # li is now [1, 2]
li.pop()        # => 3 and li is now [1, 2, 4]
li2 = li[:]  # => li2 = [1, 2, 4, 3] but (li2 is li) will result in false.
del li[2]  # li is now [1, 2, 3]
li.remove(2)  # li is now [1, 3]
li.insert(1, 2)  # li is now [1, 2, 3] again
li.index(2)  # => 1

tup = (1, 2, 3)
a, b, c = (1, 2, 3)  # a is now 1, b is now 2 and c is now 3
a, *b, c = (1, 2, 3, 4)  # a is now 1, b is now [2, 3] and c is now 4
d, e, f = 4, 5, 6
e, d = d, e  # d is now 5 and e is now 4

empty_dict = {}
filled_dict = {"one": 1, "two": 2, "three": 3}
valid_dict = {(1,2,3):[1,2,3]}   # Values can be of any type, however.
filled_dict["one"]  # => 1
list(filled_dict.keys())  # => ["three", "two", "one"]
list(filled_dict.values())  # => [3, 2, 1]
filled_dict.get("one")      # => 1
filled_dict.get("four")     # => None
filled_dict.get("four", 4)  # => 4

filled_dict.setdefault("five", 5)  # filled_dict["five"] is set to 5
filled_dict.setdefault("five", 6)  # filled_dict["five"] is still 5

# Adding to a dictionary
filled_dict.update({"four":4})  # => {"one": 1, "two": 2, "three": 3, "four": 4}
filled_dict["four"] = 4         # another way to add to dict

# Remove keys from a dictionary with del
del filled_dict["one"]  # Removes the key "one" from filled dict

some_set = {1, 1, 2, 2, 3, 4}  # some_set is now {1, 2, 3, 4}
valid_set = {(1,), 1}
filled_set = some_set
filled_set.add(5)  # filled_set is now {1, 2, 3, 4, 5}
other_set = {3, 4, 5, 6}
filled_set & other_set  # => {3, 4, 5}
filled_set | other_set  # => {1, 2, 3, 4, 5, 6}
{1, 2, 3, 4} - {2, 3, 5}  # => {1, 4}
{1, 2, 3, 4} ^ {2, 3, 5}  # => {1, 4, 5}
{1, 2} >= {1, 2, 3} # => False
{1, 2} <= {1, 2, 3} # => True
2 in filled_set   # => True
10 in filled_set  # => False




# Python offers a fundamental abstraction called the Iterable.
# An iterable is an object that can be treated as a sequence.
# The object returned by the range function, is an iterable.

filled_dict = {"one": 1, "two": 2, "three": 3}
our_iterable = filled_dict.keys()
print(our_iterable)  # => dict_keys(['one', 'two', 'three']). This is an object that implements our Iterable interface.

# We can loop over it.
for i in our_iterable:
    print(i)  # Prints one, two, three

# However we cannot address elements by index.
our_iterable[1]  # Raises a TypeError

# An iterable is an object that knows how to create an iterator.
our_iterator = iter(our_iterable)

# Our iterator is an object that can remember the state as we traverse through it.
# We get the next object with "next()".
next(our_iterator)  # => "one"

# It maintains state as we iterate.
next(our_iterator)  # => "two"
next(our_iterator)  # => "three"

# After the iterator has returned all of its data, it raises a StopIteration exception
next(our_iterator)  # Raises StopIteration

# You can grab all the elements of an iterator by calling list() on it.
list(filled_dict.keys())  # => Returns ["one", "two", "three"]


def varargs(*args):
    return args

varargs(1, 2, 3)  # => (1, 2, 3)

# You can define functions that take a variable number of
# keyword arguments, as well
def keyword_args(**kwargs):
    return kwargs

# Let's call it to see what happens
keyword_args(big="foot", loch="ness")  # => {"big": "foot", "loch": "ness"}


# You can do both at once, if you like
def all_the_args(*args, **kwargs):
    print(args)
    print(kwargs)
"""
all_the_args(1, 2, a=3, b=4) prints:
    (1, 2)
    {"a": 3, "b": 4}
"""

# When calling functions, you can do the opposite of args/kwargs!
# Use * to expand tuples and use ** to expand kwargs.
args = (1, 2, 3, 4)
kwargs = {"a": 3, "b": 4}
all_the_args(*args)            # equivalent to all_the_args(1, 2, 3, 4)
all_the_args(**kwargs)         # equivalent to all_the_args(a=3, b=4)
all_the_args(*args, **kwargs)  # equivalent to all_the_args(1, 2, 3, 4, a=3, b=4)



# There are also anonymous functions
(lambda x: x > 2)(3)                  # => True
(lambda x, y: x ** 2 + y ** 2)(2, 1)  # => 5

# There are built-in higher order functions
list(map(add_10, [1, 2, 3]))          # => [11, 12, 13]
list(map(max, [1, 2, 3], [4, 2, 1]))  # => [4, 2, 3]

list(filter(lambda x: x > 5, [3, 4, 5, 6, 7]))  # => [6, 7]

# We can use list comprehensions for nice maps and filters
# List comprehension stores the output as a list which can itself be a nested list
[add_10(i) for i in [1, 2, 3]]         # => [11, 12, 13]
[x for x in [3, 4, 5, 6, 7] if x > 5]  # => [6, 7]

# You can construct set and dict comprehensions as well.
{x for x in 'abcddeef' if x not in 'abc'}  # => {'d', 'e', 'f'}
{x: x**2 for x in range(5)}  # => {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}


import math
dir(math)

def say(msg):
    print("{name}: {message}".format(name=self.name, message=msg))


# Generators help you make lazy code.
def double_numbers(iterable):
    for i in iterable:
        yield i + i

values = (-x for x in [1,2,3,4,5])