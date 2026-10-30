# Variables
name = "Beau"
age = 39

# Expressions & statements, comments
1 + 1                       # expression
name = "Beau"; print(name)  # two statements on one line with semicolon
# this is a commented line
print(name)                 # inline comment

# Data types
print(type(name))
print(type(name) == str)
print(isinstance(name, str))

age = 2
print(isinstance(age, int))
print(isinstance(age, float))      # False

age = float(2)
print(isinstance(age, float))      # True

age = "20"
print(isinstance(age, int))        # False

age = int("20")
print(isinstance(age, int))        # True

num = "20"
age = int(num)
print(isinstance(age, int))

# Arithmetic operators
1 + 1
2 - 1
2 * 2
4 / 2
4 % 3        
4 ** 2       
5 // 2       
1 + -1

phrase = "Scamp" + " is a good dog"
print(phrase)

age = 8
age += 8
print(age)   # 16
age *= 8
print(age)   # 128

# Comparison operators
a, b = 1, 2
a == b
a != b
a > b
a <= b

# Boolean operators / "or" and "and" return operands
print(0 or 2)       # 2
print(1 or 2)       # 1
print([] or False)  # False
print(False or False)
print(0 and 2)      # 0
print(1 and 2)      # 2

# Ternary operator
def is_adult(age):
    if age > 18:
        return True
    else:
        return False


def is_adult2(age):
    return True if age > 18 else False

# Strings
phrase = "Beau"
phrase = phrase + " is my name"

name = "Beau"
print(name + " is my name")

name += " is my name"
print(name)

age = 8
print(str(age))

print("""Beau is 39 years old""")

print('''Beau is 39 years old''')

# String methods
name = "Beau"
print(name.upper())
print("Beau".lower())
print("Beau person".title())
print(name.islower())
# isalpha(), isalnum(), isdecimal(), isupper(), istitle(), startswith(), endswith(), replace(), split(), strip(), join(), find()

name = "Beau"
print(name.lower())
print(name)          

print(len(name))
print("au" in "Beau")

# Escaping
print("Beau said \"hi\"")
print('Beau said "hi" and it\'s fine')
print("B\nau")        # newline
print("B\\au")        # literal backslash

# Characters & slicing
name = "Beau"
print(name[1])        # e
print(name[0])        # B
print(name[-1])       # u
print(name[1:2])      # e
print(name[1:3])      # ea
phrase = "Beau is cool"
print(phrase[:7])
print(phrase[7:])

# Booleans
done = True
if done:
    print("yes")
else:
    print("no")

done = False

# truthiness
if 0:
    print("true")
else:
    print("false")
if -1:
    print("true")
if "Beau":
    print("true")
if "":
    print("true")
else:
    print("false")

done = True
print(type(done) == "Bool")

Book1_read = True
Book2_read = False
read_any_Book = any([Book1_read, Book2_read])
read_all_Books = all([Book1_read, Book2_read])
print(read_any_Book, read_all_Books)

# Numbers
complex_num = 2 + 3j
num = complex(2, 3)
print(num.real)
print(num.imag)

print(abs(-5.5))     
print(round(5.5))   
print(round(4.9))    
print(round(5.49, 1))

# Enums
from enum import Enum
class State(Enum):
    INACTIVE = 0
    ACTIVE = 1
print(State.ACTIVE)
print(State.ACTIVE.value)
print(State(1))
print(State["ACTIVE"])
print(list(State))
print(len(State))

# User input
age = input("What is your age? ")
print("Your age is " + age)

# Ctrl statements
condition = True
if condition == True:
    print("The condition")
    print("was true")
else:
    print("The condition")
    print("was false")
print("outside if")

name = "Flavio"
if name == "Roger":
    print("Hello Roger")
elif name == "Syd":
    print("Hello Syd")
else:
    print("Hello " + name)

# Lists
dogs = ["Roger", "Syd"]
items = ["Roger", 1, "Syd", True]
print("Roger" in dogs)
empty_list = []

dogs = ["Roger", 1, "Syd", True]
print(dogs[0])
print(dogs[2])
dogs[2] = "Beau"
print(dogs)
print(dogs[-1])
print(dogs[2:4])
print(dogs[2:])
print(dogs[:3])
print(len(dogs))

dogs.append("Judah")
dogs.extend(["Tina", "Quincy"])
dogs += ["Tina", "Quincy"]
dogs += ["Iron"]       # keep the brackets, Iron alone would add each letter
dogs.remove("Quincy")
print(dogs.pop())      # removes and returns last item

items = ["Roger", 1, "Syd", True]
items.insert(2, "Test")
items[1:1] = ["Test1", "Test2"]    # insert multiple items at index

# Sorting
items = ["Roger", "Beaub", "Syd", "Test"]
items.sort()
items.sort(key=str.lower)           # case-insensitive
items_copy = items[:]               # copy before sorting
print(sorted(items, key=str.lower)) # new list, original untouched

# Tuples
names = ("Roger", "Syd")
print(names[0])
print(names.index("Roger"))
print(names[-1])
print(len(names))
print("Roger" in names)
print(names[0:2])
print(sorted(names))
new_tuple = names + ("Tina", "Quincy")

# Dictionaries
dog = {"name": "Roger"}
dog = {"name": "Roger", "age": 8}
print(dog["name"])
dog["name"] = "Syd"
print(dog.get("name"))
print(dog.get("color", "brown"))

dog["color"] = "green"
print(dog.pop("name"))
print(dog)
print(dog.popitem())
print("color" in dog)
print(list(dog.keys()))
print(list(dog.values()))
print(list(dog.items()))
print(len(dog))
dog["favorite food"] = "Meat"
del dog["favorite food"]
dog_copy = dog.copy()

# Sets
set1 = {"Roger", "Syd"}
set2 = {"Roger"}

intersect = set1 & set2          # {'Roger'}
mod = set1 | set2                # union
mod = set1 - set2                # difference {'Syd'}
print(set1 > set2)               # superset  True
print(set1 < set2)               # subset    False
print(len(set1))
print(list(set1))
print("Roger" in set1)
print({"Roger", "Syd", "Roger"})  # duplicates dropped

# Functions
def hello():
    print("Hello!")

hello()
hello()
hello()


def hello(name):
    print("Hello " + name)

hello("Beau")
hello("Quincy")


def hello(name="my friend"):
    print("Hello " + name)

hello("Beau")
hello()


def hello(name, age):
    print("Hello " + name + ", you are " + str(age) + " years old")

hello("Beau", 39)


# immutable parameter - change does not leak outside
def change(value):
    value = 2

val = 1
change(val)
print(val)   


# mutable parameter - change is reflected outside
def change(value):
    value["name"] = "Syd"

val = {"name": "Beau"}
change(val)
print(val)   


# return values
def hello(name):
    print("Hello " + name)
    return name

hello("Syd")


def hello(name):
    if not name:
        return
    print("Hello " + name)

hello(False)
hello("Beau")


def hello(name):
    print("Hello " + name)
    return name, "Beau", 8

print(hello("Syd"))   

# Variable scope
age = 8

def test():
    print(age)

print(age)
test()


def test():
    age = 8
    print(age)

test()
# print(age)  # NameError: name 'age' is not defined

# Nested functions
def talk(phrase):
    def say(word):
        print(word)

    words = phrase.split(" ")
    for word in words:
        say(word)

talk("I am going to buy the milk")

def count():
    count = 0

    def increment():
        nonlocal count
        count = count + 1
        print(count)

    increment()

count()

# Closures
def counter():
    count = 0

    def increment():
        nonlocal count
        count = count + 1
        return count

    return increment

increment = counter()

print(increment()) 
print(increment()) 
print(increment()) 

# Objects
age = 8
print(age.real)
print(age.imag)
print(age.bit_length())

items = [1, 2]
items.append(3)
items.append(4)
print(items.pop())
print(id(items))

age = age + 1   # creates a new int object

# Loops
# while True: infinite loop
#     print("The condition is true")

condition = True
while condition == True:
    print("The condition is true")
    condition = False
print("After the loop")

count = 0
while count < 10:
    print("The condition is true")
    count += 1

items = [1, 2, 3, 4]
for item in items:
    print(item)

for item in range(15):
    print(item)

for index, item in enumerate(items):
    print(index, item)

names = ["Roger", "Syd"]
for index, name in enumerate(names):
    print(index, name)

# break and continue
items = [1, 2, 3, 4]
for item in items:
    if item == 2:
        continue
    print(item)       

for item in items:
    if item == 2:
        break
    print(item)       

# Classes
class Animal:
    def walk(self):
        print("Walking...")


class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("WOF!")


roger = Dog("Roger", 8)
print(type(roger))
print(roger.name)
print(roger.age)
roger.bark()
roger.walk()

# Modules
# --- dog.py ---
# def bark():
#     print("WOF!")
#
# --- main.py ---
# import dog
# dog.bark()
#
# from dog import bark
# bark()
#
# If dog.py lives in a subfolder "lib" (with an empty __init__.py in it):
# from lib import dog
# dog.bark()
#
# from lib.dog import bark
# bark()

# Standard library
import math
print(math.sqrt(4))

from math import sqrt
print(sqrt(4))

# Arguments from the command line
# run with:  python main.py Beau 39
import sys

print(sys.argv)
name = sys.argv[1]
print("Hello " + name)

# argparse
import argparse

parser = argparse.ArgumentParser(
    description="This program prints the name of my dogs"
)
parser.add_argument("-c", "--color", metavar="color", required=True,
                    choices={"red", "yellow"}, help="the color to search for")
args = parser.parse_args()
print(args.color)
# run with: python main.py -c red

# Lambda functions
double = lambda num: num * 2
multiply = lambda a, b: a * b
print(multiply(2, 4))   # 8

# map, filter, reduce
numbers = [1, 2, 3]

def double(a):
    return a * 2

result = map(double, numbers)
print(list(result))                       

double = lambda a: a * 2
result = map(double, numbers)
print(list(result))

print(list(map(lambda a: a * 2, numbers)))

# filter
numbers = [1, 2, 3, 4, 5, 6]

def isEven(n):
    return n % 2 == 0

result = filter(isEven, numbers)
print(list(result))

print(list(filter(lambda n: n % 2 == 0, numbers)))

# reduce
expenses = [
    ("Dinner", 80),
    ("Car repair", 120)
]

sum = 0
for expense in expenses:
    sum += expense[1]
print(sum)

from functools import reduce
sum = reduce(lambda a, b: a + b[1], expenses, 0)
print(sum)  

# Recursion
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(3))   
print(factorial(4))   
print(factorial(5))   

# Decorators
def logtime(func):
    def wrapper():
        # do something before
        print("before")
        val = func()
        # do something after
        print("after")
        return val

    return wrapper
@logtime
def hello():
    print("hello!")
hello()

# Docstrings
"""Dog module

This module does ... and provides the following classes: Dog
...
"""
class Dog:
    """A class representing a dog"""
    def __init__(self, name, age):
        """Initialize a new dog"""
        self.name = name
        self.age = age
    def bark(self):
        """Let the dog bark"""
        print("WOF!")
print(help(Dog))

# Annotations
def increment(n):
    return n + 1
def increment(n: int) -> int:
    return n + 1
count: int = 0

# Exceptions
# Structure:
# try:
#     # some lines of code
# except <ERROR1>:
#     # handler <ERROR1>
# except <ERROR2>:
#     # handler <ERROR2>
# except:
#     # catch all other exceptions
# else:
#     # no exceptions were raised
# finally:
#     # always runs

# result = 2 / 0       # ZeroDivisionError
# print(result)

try:
    result = 2 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    result = 1

print(result)

# raise
# raise Exception("An error occurred!")

try:
    raise Exception("An error")
except Exception as error:
    print(error)


# custom exception
class DogNotFoundException(Exception):
    pass


try:
    raise DogNotFoundException()
except DogNotFoundException:
    print("Dog not found!")


class DogNotFoundException(Exception):
    print("inside")

try:
    raise DogNotFoundException()
except DogNotFoundException:
    print("Dog not found!")

# The with statement
filename = "test.txt"   # any existing file

try:
    file = open(filename, "r")
    content = file.read()
    print(content)
finally:
    file.close()

with open(filename, "r") as file:
    content = file.read()
    print(content)

# Installing packages with pip (run in terminal, not Python)
# pip install requests
# pip install -U requests
# pip install requests==2.28.0
# pip uninstall requests
# pip show requests

# List comprehensions
numbers = [1, 2, 3, 4, 5]
numbers_power_2 = [n**2 for n in numbers]
print(numbers_power_2)   # [1, 4, 9, 16, 25]
# same with a loop
numbers_power_2 = []
for n in numbers:
    numbers_power_2.append(n**2)
# same with map
numbers_power_2 = list(map(lambda n: n**2, numbers))

# Polymorphism
class Dog:
    def eat(self):
        print("Eating dog food")
class Cat:
    def eat(self):
        print("Eating cat food")
animal1 = Dog()
animal2 = Cat()
animal1.eat()
animal2.eat()

# Operator overloading
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __gt__(self, other):
        return True if self.age > other.age else False


roger = Dog("Roger", 8)
syd = Dog("Syd", 7)

print(roger > syd)   # True
# Other special methods: __eq__, __lt__, __le__, __ge__, __ne__, __add__, __sub__, __mul__, __truediv__, __floordiv__, __mod__, __pow__ ...