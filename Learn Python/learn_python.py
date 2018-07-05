# is checks if two variables refer to the same object, but == checks
# if the objects pointed to have the same values.


# Equivalent of C's '?:' ternary operator
"yahoo!" if 3 > 2 else 2  # yahoo!


li = []
li2 = li[:]     # => li2 = [1, 2, 4, 3] but (li2 is li) will result in false.
del li[2]       # li is now [1, 2, 3]
li.remove(2)    # li is now [1, 3]
li.insert(1, 2) # li is now [1, 2, 3] again
li.index(2)     # => 1


tup = (1, 2, 3)
a, b, c = (1, 2, 3)  # a is now 1, b is now 2 and c is now 3
a, *b, c = (1, 2, 3, 4)  # a is now 1, b is now [2, 3] and c is now 4
d, e, f = 4, 5, 6
e, d = d, e  # d is now 5 and e is now 4


empty_dict = {}
filled_dict = {"one": 1, "two": 2, "three": 3}
valid_dict = {(1,2,3):[1,2,3]}   # Values can be of any type, however.
filled_dict["one"]          # => 1
list(filled_dict.keys())    # => ["three", "two", "one"]
list(filled_dict.values())  # => [3, 2, 1]
filled_dict.get("one")      # => 1
filled_dict.get("four")     # => None
filled_dict.get("four", 4)  # => 4

filled_dict.setdefault("five", 5)  # filled_dict["five"] is set to 5
filled_dict.setdefault("five", 6)  # filled_dict["five"] is still 5

filled_dict.update({"four":4})  # => {"one": 1, "two": 2, "three": 3, "four": 4}
filled_dict["four"] = 4         # another way to add to dict

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


filled_dict = {"one": 1, "two": 2, "three": 3}
our_iterable = filled_dict.keys()
print(our_iterable)  # => dict_keys(['one', 'two', 'three])

for i in our_iterable:
    print(i)

our_iterator = iter(our_iterable)
next(our_iterator)  # one
next(our_iterator)  # two
next(our_iterator)  # three
next(our_iterator)  # Raises StopIteration


# infinite arguments like printf
def varargs(*args):
    return args

# arguments as a dictionary
def keyword_args(**kwargs):
    return kwargs

keyword_args(big="foot", loch="ness")  # => {"big": "foot", "loch": "ness"}

def all_the_args(*args, **kwargs):
    print(args)
    print(kwargs)

all_the_args(1, 2, a=3, b=4)
"""
    (1, 2)
    {"a": 3, "b": 4}
"""


# There are also anonymous functions
(lambda x: x > 2)(3)                  # => True
(lambda x, y: x ** 2 + y ** 2)(2, 1)  # => 5

# You can construct set and dict comprehensions as well.
{x for x in 'abcddeef' if x not in 'abc'}  # => {'d', 'e', 'f'}
{x: x**2 for x in range(5)}  # => {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}


import math
dir(math)  # lists all functions

# printf style arguments
def say(msg):
    print("{name}: {message}".format(name=self.name, message=msg))


# Generators help you make lazy code.
def double_numbers(iterable):
    for i in iterable:
        yield i + i

values = (-x for x in [1,2,3,4,5])