# EXCEPTIONS AND ERRORS
# Syntax errors (these won't run):
# a = 5 print(a)          SyntaxError
# a = 5 print(a))         SyntaxError (extra parenthesis)

# Exceptions (each line below raises):
# a = 5 + "10"                            # TypeError
# import somemodule                       # ModuleNotFoundError (subclass of ImportError)
# a = 5
# b = c                                   # NameError
# f = open("somefile.txt")                # FileNotFoundError
# a = [1, 2, 3]
# a.remove(4)                             # ValueError: list.remove(x): x not in list
# a[4]                                    # IndexError: list index out of range
# my_dict = {"name": "Max"}
# my_dict["age"]                          # KeyError

# raise
x = -5
if x < 0:
    raise Exception("x should be positive")

# assert
assert (x >= 0), "x is not positive"

# try / except
try:
    a = 5 / 0
except:
    print("an error happened")

try:
    a = 5 / 0
except Exception as e:
    print(e)

try:
    a = 5 / 0
except ZeroDivisionError as e:
    print(e)

try:
    a = 5 / 1
    b = a + "10"
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)

# else and finally
try:
    a = 5 / 1
    b = a + 4
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print("everything is fine")
finally:
    print("cleaning up...")

# custom exceptions
class ValueTooHighError(Exception):
    pass


class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


def test_value(x):
    if x > 100:
        raise ValueTooHighError("value is too high")
    if x < 5:
        raise ValueTooSmallError("value is too small", x)

try:
    test_value(200)
except ValueTooHighError as e:
    print(e)

try:
    test_value(1)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)

# LOGGING
import logging

logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S",
)

# helper.py 
# import logging
# logger = logging.getLogger(__name__)
# logger.info("hello from helper")
# logger.propagate = False      # (optional) stop messages going to root logger
#
# main.py 
# import logging
# logging.basicConfig(level=logging.DEBUG, format="%(name)s - %(levelname)s - %(message)s")
# import helper

# handlers
logger = logging.getLogger(__name__)

stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler("file.log")

stream_handler.setLevel(logging.WARNING)
file_handler.setLevel(logging.ERROR)

formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

logger.warning("this is a warning")
logger.error("this is an error")

# logging.conf (RECONSTRUCTED - the file was shown only briefly)
# [loggers]
# keys=root,simpleExample
#
# [handlers]
# keys=consoleHandler
#
# [formatters]
# keys=simpleFormatter
#
# [logger_root]
# level=DEBUG
# handlers=consoleHandler
#
# [logger_simpleExample]
# level=DEBUG
# handlers=consoleHandler
# qualname=simpleExample
# propagate=0
#
# [handler_consoleHandler]
# class=StreamHandler
# level=DEBUG
# formatter=simpleFormatter
# args=(sys.stdout,)
#
# [formatter_simpleFormatter]
# format=%(asctime)s - %(name)s - %(levelname)s - %(message)s

import logging.config

logging.config.fileConfig("logging.conf")
logger = logging.getLogger("simpleExample")
logger.debug("this is a debug message")

# stack traces
try:
    a = [1, 2, 3]
    val = a[4]
except IndexError as e:
    logging.error(e, exc_info=True)

import traceback

try:
    a = [1, 2, 3]
    val = a[4]
except:
    logging.error("The error is %s", traceback.format_exc())

# rotating file handler
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = RotatingFileHandler("app.log", maxBytes=2000, backupCount=5)
logger.addHandler(handler)

for _ in range(10000):
    logger.info("Hello, world!")

# timed rotating file handler
import time
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# when: "s" seconds, "m" minutes, "h" hours, "d" days, "midnight", "w0"
handler = TimedRotatingFileHandler("timed_test.log", when="s", interval=5, backupCount=5)
logger.addHandler(handler)

for _ in range(6):
    logger.info("Hello, world!")
    time.sleep(5)

# JSON logging: pip install python-json-logger, then add its formatter to your handler
# JSON
import json

person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hasChildren": False,
    "titles": ["engineer", "programmer"],
}

# encode (serialize)
personJSON = json.dumps(person)
print(personJSON)
personJSON = json.dumps(person, indent=4)
print(personJSON)
personJSON = json.dumps(person, indent=4, separators=("; ", "= "))   # not recommended
print(personJSON)
personJSON = json.dumps(person, indent=4, sort_keys=True)
print(personJSON)

with open("person.json", "w") as file:
    json.dump(person, file)
with open("person.json", "w") as file:
    json.dump(person, file, indent=4)

# decode (deserialize)
person = json.loads(personJSON)
print(person)

with open("person.json", "r") as file:
    person = json.load(file)
    print(person)

# custom objects
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User("Max", 27)
# userJSON = json.dumps(user)    # TypeError: Object of type User is not JSON serializable


def encode_user(o):
    if isinstance(o, User):
        return {"name": o.name, "age": o.age, o.__class__.__name__: True}
    else:
        raise TypeError("Object of type User is not JSON serializable")

userJSON = json.dumps(user, default=encode_user)
print(userJSON)

from json import JSONEncoder

class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {"name": o.name, "age": o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)

userJSON = json.dumps(user, cls=UserEncoder)
print(userJSON)

userJSON = UserEncoder().encode(user)
print(userJSON)

# decode into custom object
user = json.loads(userJSON)
print(type(user))      


def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct["name"], age=dct["age"])
    return dct

user = json.loads(userJSON, object_hook=decode_user)
print(type(user))
print(user.name)

# RANDOM NUMBERS
import random

a = random.random()                 # float in [0, 1)
print(a)
a = random.uniform(1, 10)           # float in range
print(a)
a = random.randint(1, 10)           # upper bound INCLUDED
print(a)
a = random.randrange(1, 10)         # upper bound excluded
print(a)
a = random.normalvariate(0, 1)      # mu=0, sigma=1
print(a)

my_list = list("ABCDEFGH")
print(my_list)
a = random.choice(my_list)
print(a)
a = random.sample(my_list, 3)       # unique elements
print(a)
a = random.choices(my_list, k=3)    # may repeat
print(a)

random.shuffle(my_list)             # in place
print(my_list)

# reproducible with seed
random.seed(1)
print(random.random())
print(random.randint(1, 10))

random.seed(2)
print(random.random())
print(random.randint(1, 10))

random.seed(1)
print(random.random())
print(random.randint(1, 10))

random.seed(2)
print(random.random())
print(random.randint(1, 10))

# secrets (cryptographically strong)
import secrets

a = secrets.randbelow(10)           
print(a)
a = secrets.randbits(4)             
print(a)
my_list = list("ABCDEFGH")
a = secrets.choice(my_list)
print(a)

# numpy random (pip install numpy)
import numpy as np

np.random.seed(1)
a = np.random.rand(3)               # 1d, 3 floats
print(a)
a = np.random.rand(3, 3)            # 3x3
print(a)
a = np.random.randint(0, 10, 3)     # 10 excluded
print(a)
a = np.random.randint(0, 10, (3, 4))
print(a)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)
np.random.shuffle(arr)              # shuffles along first axis only
print(arr)

np.random.seed(1)
print(np.random.rand(3, 3))
np.random.seed(1)
print(np.random.rand(3, 3))         # same array