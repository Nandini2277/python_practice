# LISTS
my_list = ["banana", "cherry", "apple"]
print(my_list)

my_list2 = list()
print(my_list2)

my_list = [5, True, "apple", "apple"]     # mixed types, duplicates allowed
print(my_list)

my_list = ["banana", "cherry", "apple"]
item = my_list[0]
print(item)
# item = my_list[3]    # IndexError: list index out of range
item = my_list[-1]     # last item
print(item)

for i in my_list:
    print(i)

if "banana" in my_list:
    print("yes")
else:
    print("no")

print(len(my_list))
my_list.append("lemon")
print(my_list)
my_list.insert(1, "blueberry")
print(my_list)

item = my_list.pop()               # removes and returns last item
print(item)
print(my_list)

my_list.remove("cherry")
print(my_list)
# my_list.remove("cherrr")         # ValueError: not in list

my_list.clear()
print(my_list)

my_list = ["banana", "cherry", "apple"]
my_list.reverse()
print(my_list)

my_list = [3, 2, 1, 4, -1, -5, 10]
my_list.sort()                     # in place
print(my_list)

my_list = [3, 2, 1, 4, -1, -5, 10]
new_list = sorted(my_list)         # new list
print(my_list)
print(new_list)

my_list = [0] * 5
print(my_list)

my_list2 = [1, 2, 3, 4, 5]
new_list = my_list + my_list2
print(new_list)

# slicing
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = my_list[1:5]
print(a)
a = my_list[:5]
a = my_list[1:]
a = my_list[::1]
a = my_list[::2]
a = my_list[::-1]                  # reverse
print(a)

# copying
list_org = ["banana", "cherry", "apple"]
list_copy = list_org               # same reference
list_copy.append("lemon")
print(list_copy)
print(list_org)

list_org = ["banana", "cherry", "apple"]
list_copy = list_org.copy()
list_copy = list(list_org)
list_copy = list_org[:]
list_copy.append("lemon")
print(list_copy)
print(list_org)

# list comprehension
my_list = [1, 2, 3, 4, 5, 6]
b = [i * i for i in my_list]
print(my_list)
print(b)

# TUPLES
my_tuple = ("Max", 28, "Boston")
print(my_tuple)
my_tuple = "Max", 28, "Boston"      # parentheses optional

my_tuple = ("Max")
print(type(my_tuple))               # <class 'str'>
my_tuple = ("Max",)                 # trailing comma needed
print(type(my_tuple))               # <class 'tuple'>

my_tuple = tuple(["Max", 28, "Boston"])
print(my_tuple)

my_tuple = ("Max", 28, "Boston")
item = my_tuple[0]
print(item)
item = my_tuple[-1]
print(item)

# my_tuple[0] = "Tim"               # TypeError: no item assignment

for i in my_tuple:
    print(i)

if "Max" in my_tuple:
    print("yes")
else:
    print("no")

my_tuple = ("a", "p", "p", "l", "e")
print(len(my_tuple))
print(my_tuple.count("p"))
print(my_tuple.index("p"))

my_list = list(my_tuple)
print(my_list)
my_tuple2 = tuple(my_list)
print(my_tuple2)

a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b = a[2:5]
print(b)
b = a[::2]
b = a[::-1]                         # reverse

# unpacking
my_tuple = ("Max", 28, "Boston")
name, age, city = my_tuple
print(name)
print(age)
print(city)

my_tuple = (0, 1, 2, 3, 4)
i1, *i2, i3 = my_tuple
print(i1)
print(i2)    # [1, 2, 3]  (a list)
print(i3)

# list vs tuple: size and speed
import sys
my_list = [0, 1, 2, "hello", True]
my_tuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")

import timeit
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))

# DICTIONARIES
my_dict = {"name": "Max", "age": 28, "city": "New York"}
print(my_dict)

my_dict2 = dict(name="Mary", age=27, city="Boston")
print(my_dict2)

value = my_dict["name"]
print(value)
value = my_dict["age"]
print(value)
# value = my_dict["lastname"]       # KeyError

my_dict["email"] = "max@xyz.com"
print(my_dict)
my_dict["email"] = "coolmax@xyz.com"   # overwrite
print(my_dict)

del my_dict["email"]
print(my_dict)
my_dict.pop("age")
print(my_dict)
my_dict.popitem()                   # removes last inserted item (3.7+)
print(my_dict)

my_dict = {"name": "Max", "age": 28, "city": "New York"}
if "name" in my_dict:
    print(my_dict["name"])

try:
    print(my_dict["lastname"])
except:
    print("error")

for key in my_dict:
    print(key)
for key in my_dict.keys():
    print(key)
for value in my_dict.values():
    print(value)
for key, value in my_dict.items():
    print(key, value)

# copying
my_dict_copy = my_dict              # same reference
my_dict_copy["email"] = "max@xyz.com"
print(my_dict_copy)
print(my_dict)

my_dict = {"name": "Max", "age": 28, "city": "New York"}
my_dict_copy = my_dict.copy()
my_dict_copy["email"] = "max@xyz.com"
print(my_dict_copy)
print(my_dict)

my_dict_copy = dict(my_dict)

# merging with update
my_dict = {"name": "Max", "age": 28, "email": "max@xyz.com"}
my_dict2 = dict(name="Mary", age=27, city="Boston")
my_dict.update(my_dict2)
print(my_dict)

# key types
my_dict = {3: 9, 6: 36, 9: 81}
print(my_dict)
# value = my_dict[0]                # KeyError
value = my_dict[3]
print(value)

my_tuple = (8, 7)
my_dict = {my_tuple: 15}
print(my_dict)

# my_list = [8, 7]
# my_dict = {my_list: 15}           # TypeError: unhashable type: 'list'

# SETS
my_set = {1, 2, 3}
print(my_set)
my_set = {1, 2, 1, 2, 3}            # duplicates dropped
print(my_set)

my_set = set([1, 2, 1, 2, 3])
print(my_set)
my_set = set("Hello")
print(my_set)

a = {}                              # this is a dict
print(type(a))
a = set()                           # empty set
print(type(a))

my_set = set()
my_set.add(1)
my_set.add(2)
my_set.add(3)
print(my_set)

my_set.remove(3)                    # KeyError if missing
my_set.discard(4)                   # no error if missing
my_set.clear()

my_set = {1, 2, 3}
print(my_set.pop())                 # arbitrary element
print(my_set)

for i in my_set:
    print(i)
if 1 in my_set:
    print("yes")

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)
i = odds.intersection(evens)
print(i)
i = odds.intersection(primes)
print(i)
i = evens.intersection(primes)
print(i)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

diff = setA.difference(setB)
print(diff)
diff = setB.difference(setA)
print(diff)
diff = setA.symmetric_difference(setB)
print(diff)

setA.update(setB)
print(setA)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setA.intersection_update(setB)
print(setA)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setA.difference_update(setB)
print(setA)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setA.symmetric_difference_update(setB)
print(setA)

setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
print(setA.issubset(setB))          # False
print(setB.issubset(setA))          # True
print(setA.issuperset(setB))        # True
print(setB.issuperset(setA))        # False

setC = {7, 8}
print(setA.isdisjoint(setB))        # False
print(setA.isdisjoint(setC))        # True

# copying
setA = {1, 2, 3, 4, 5, 6}
setB = setA                         # same reference
setB.add(7)
print(setB)
print(setA)

setA = {1, 2, 3, 4, 5, 6}
setB = setA.copy()
setB.add(7)
setB = set(setA)

# frozenset
a = frozenset([1, 2, 3, 4])
print(a)
# a.add(2)        error
# a.remove(1)     error
# frozensets still support union/intersection/difference

# STRINGS
my_string = "Hello World"
my_string = 'Hello World'
my_string = 'I\'m a programmer'
my_string = "I'm a programmer"
my_string = """Hello
World"""
my_string = "Hello \
World"

my_string = "Hello World"
char = my_string[0]
print(char)
char = my_string[-1]
print(char)
# my_string[0] = "h"   # TypeError: strings are immutable

substring = my_string[1:5]
print(substring)
substring = my_string[::2]
substring = my_string[::-1]         # reverse
print(substring)

greeting = "Hello"
name = "Tom"
sentence = greeting + " " + name
print(sentence)

for i in greeting:
    print(i)

if "e" in greeting:
    print("yes")
else:
    print("no")
if "ell" in greeting:
    print("yes")

my_string = "     Hello World    "
my_string = my_string.strip()       # assign back: strings are immutable
print(my_string)
print(my_string.upper())
print(my_string.lower())
print(my_string.startswith("H"))
print(my_string.startswith("Hello"))
print(my_string.startswith("World"))
print(my_string.endswith("World"))
print(my_string.find("o"))          # 4
print(my_string.find("llo"))
print(my_string.find("xyz"))        # -1
print(my_string.count("o"))
print(my_string.count("p"))
print(my_string.replace("World", "Universe"))

my_string = "how are you doing"
my_list = my_string.split()
print(my_list)
my_string = "how,are,you,doing"
my_list = my_string.split(",")
print(my_list)

new_string = " ".join(my_list)
print(new_string)

# join vs += (join is much faster)
from timeit import default_timer as timer

my_list = ["a"] * 1000000

start = timer()
my_string = ""
for i in my_list:
    my_string += i
stop = timer()
print(stop - start)

start = timer()
my_string = "".join(my_list)
stop = timer()
print(stop - start)

# formatting
var = "Tom"
my_string = "the variable is %s" % var
print(my_string)

var = 3
my_string = "the variable is %d" % var
var = 3.1234567
my_string = "the variable is %f" % var
my_string = "the variable is %.2f" % var
print(my_string)

var = 3.1234567
my_string = "the variable is {}".format(var)
my_string = "the variable is {:.2f}".format(var)
var2 = 6
my_string = "the variables are {} {}".format(var, var2)
print(my_string)

# f-strings (3.6+)
my_string = f"the variables are {var} {var2}"
print(my_string)
my_string = f"the variables are {var} {var2 * 2}"
print(my_string)