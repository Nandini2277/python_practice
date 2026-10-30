# FUNCTION ARGUMENTS
def print_name(name):          # `name` is a parameter
    print(name)

print_name("Alex")             # "Alex" is an argument


def foo(a, b, c):
    print(a, b, c)

foo(1, 2, 3)                   # positional
foo(a=1, b=2, c=3)             # keyword
foo(c=1, b=2, a=3)             # order doesn't matter with keywords -> 3 2 1
foo(1, b=2, c=3)               # mix OK
# foo(1, b=2, 3)               # error: positional after keyword
# foo(1, a=2, c=3)             # error: multiple values for a


# default arguments (must come last)
def foo(a, b, c, d=4):
    print(a, b, c, d)

foo(1, 2, 3)                   # 1 2 3 4
foo(1, 2, 3, 7)                # 1 2 3 7

# def foo(a, b=2, c, d=4):     # error: non-default after default


# *args and **kwargs
def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])

foo(1, 2, 3, 4, 5, six=6, seven=7)
foo(1, 2)
foo(1, 2, 3, 4, 5)
foo(1, 2, six=6, seven=7)


# keyword-only arguments
def foo(a, b, *, c, d):
    print(a, b, c, d)

# foo(1, 2, 3, 4)              # error
foo(1, 2, c=3, d=4)


def foo(*args, last):
    for arg in args:
        print(arg)
    print(last)

# foo(1, 2, 3)                 # error: missing keyword-only `last`
foo(1, 2, 3, last=100)


# unpacking into arguments
def foo(a, b, c):
    print(a, b, c)

my_list = [0, 1, 2]
foo(*my_list)
my_tuple = (0, 1, 2)
foo(*my_tuple)
my_dict = {"a": 1, "b": 2, "c": 3}
foo(**my_dict)
# keys must match parameter names, count must match


# local vs global
number = 0

def foo():
    x = number
    print("number inside function:", x)

foo()


def foo():
    global number          # needed to modify the global
    number = 3

foo()
print(number)              

number = 0

def foo():
    number = 3             # creates a LOCAL variable

foo()
print(number)              


# parameter passing
def foo(x):
    x = 5                  # rebinding - outer value unchanged

var = 10
foo(var)
print(var)                 


def foo(a_list):
    a_list.append(4)       # mutates the passed list
    a_list[0] = -100

my_list = [1, 2, 3]
foo(my_list)
print(my_list)             


def foo(a_list):
    a_list = [200, 300, 400]   # rebinding - outer list unchanged
    a_list.append(4)

my_list = [1, 2, 3]
foo(my_list)
print(my_list)             


def foo(a_list):
    a_list += [4, 5]       # in-place extend -> changes outer list

my_list = [1, 2, 3]
foo(my_list)
print(my_list)

def foo(a_list):
    a_list = a_list + [4, 5]   # new list -> outer list unchanged

my_list = [1, 2, 3]
foo(my_list)
print(my_list)

# THE ASTERISK (*) OPERATOR
# multiplication and power
result = 5 * 7
print(result)
result = 2 ** 4            
print(result)

# repeated elements in list / tuple / string
zeros = [0] * 10
print(zeros)
zeros_and_ones = [0, 1] * 10
print(zeros_and_ones)
zeros_tuple = (0, 1) * 10
string = "AB" * 10
print(string)


# *args, **kwargs, keyword-only
def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])

foo(1, 2, 3, 4, 5, six=6, seven=7)


def foo(a, b, *, c):
    print(a, b, c)

foo(1, 2, c=3)


# unpacking into function arguments
def foo(a, b, c):
    print(a, b, c)

my_list = [0, 1, 2]
foo(*my_list)
my_dict = {"a": 1, "b": 2, "c": 3}
foo(**my_dict)

# unpacking containers
numbers = [1, 2, 3, 4, 5, 6]
*beginning, last = numbers
print(beginning)
print(last)

beginning, *last = numbers
print(beginning)
print(last)

beginning, *middle, last = numbers
print(beginning)
print(middle)
print(last)

*beginning, second_last, last = numbers
print(second_last)

# merging iterables into a list
my_tuple = (1, 2, 3)
my_list = [4, 5, 6]
my_set = {7, 8, 9}
new_list = [*my_tuple, *my_list, *my_set]
print(new_list)

# merging dictionaries
dict_a = {"a": 1, "b": 2}
dict_b = {"c": 3, "d": 4}
my_dict = {**dict_a, **dict_b}
print(my_dict)

# SHALLOW vs DEEP COPYING
import copy

# assignment: no real copy
org = 5
cpy = org
cpy = 6
print(cpy)
print(org)

org = [0, 1, 2, 3, 4]
cpy = org
cpy[0] = -10
print(cpy)
print(org)         # also changed

# shallow copy (one level deep)
org = [0, 1, 2, 3, 4]
cpy = copy.copy(org)
cpy[0] = -10
print(cpy)
print(org)

cpy = org.copy()
cpy = list(org)
cpy = org[:]

# nested lists: shallow copy is not enough
org = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
cpy = copy.copy(org)
cpy[0][1] = -10
print(cpy)
print(org)         # also changed

# deep copy
org = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
cpy = copy.deepcopy(org)
cpy[0][1] = -10
print(cpy)
print(org)         # unchanged


# custom objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Alex", 27)
p2 = p1
p2.age = 28
print(p2.age)
print(p1.age)      # both changed

p1 = Person("Alex", 27)
p2 = copy.copy(p1)
p2.age = 28
print(p2.age)
print(p1.age)      # p1 unchanged


class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee

boss = Person("Jane", 55)
employee = Person("Joe", 28)
company = Company(boss, employee)

company_clone = copy.copy(company)
company_clone.boss.age = 56
print(company_clone.boss.age)
print(company.boss.age)       # also 56 (shallow copy)

boss = Person("Jane", 55)
employee = Person("Joe", 28)
company = Company(boss, employee)
company_clone = copy.deepcopy(company)
company_clone.boss.age = 56
print(company_clone.boss.age)  # 56
print(company.boss.age)        # 55

# CONTEXT MANAGERS
# with open: the standard example
with open("notes.txt", "w") as file:
    file.write("some todo...")

# same thing written out
file = open("notes.txt", "w")
try:
    file.write("some todo...")
finally:
    file.close()

# lock as a context manager
from threading import Lock
lock = Lock()

lock.acquire()
# ... do something
lock.release()

with lock:
    pass   # do something


# class-based context manager
class ManagedFile:
    def __init__(self, filename):
        print("init", filename)
        self.filename = filename

    def __enter__(self):
        print("enter")
        self.file = open(self.filename, "w")
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
        print("exc:", exc_type, exc_value)
        print("exit")
        # Handle the exception ourselves:
        # if exc_type is not None:
        #     print("Exception has been handled")
        # return True   # True suppresses the exception


with ManagedFile("notes.txt") as file:
    print("doing stuff...")
    file.write("some todo...")
    # file.some_method()      # would raise AttributeError inside the with block
print("continuing")


# generator-based context manager
from contextlib import contextmanager


@contextmanager
def open_managed_file(filename):
    f = open(filename, "w")
    try:
        yield f
    finally:
        f.close()

with open_managed_file("notes.txt") as f:
    f.write("some todo...")
