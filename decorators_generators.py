import functools

# DECORATORS
# Syntax shape:
# @my_decorator
# def do_something():
#     pass


def start_end_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result
    return wrapper


@start_end_decorator
def print_name():
    print("Alex")

print_name()


@start_end_decorator
def add5(x):
    return x + 5

result = add5(10)
print(result)
print(help(add5))
print(add5.__name__)


# Template for a function decorator
def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Do something before
        result = func(*args, **kwargs)
        # Do something after
        return result
    return wrapper


# Decorator with arguments
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat


@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")

greet("Alex")


# Nested decorators
# (debug decorator was pasted off-screen in the video; this is the standard version
#  that prints name, args, kwargs, and the return value)
def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper


@debug
@start_end_decorator
def say_hello(name):
    greeting = f"Hello {name}"
    print(greeting)
    return greeting

say_hello("Alex")


# Class decorator
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"This is executed {self.num_calls} times")
        return self.func(*args, **kwargs)


@CountCalls
def say_hello_count():
    print("Hello")

say_hello_count()
say_hello_count()

# GENERATORS
def my_generator():
    yield 3
    yield 2
    yield 1

g = my_generator()
for i in g:
    print(i)

g = my_generator()
value = next(g)
print(value)
value = next(g)
print(value)
value = next(g)
print(value)
# value = next(g)    # StopIteration

g = my_generator()
print(sum(g))
g = my_generator()
print(sorted(g))


def countdown(num):
    print("Starting")
    while num > 0:
        yield num
        num -= 1

cd = countdown(4)
value = next(cd)
print(value)
print(next(cd))
print(next(cd))
print(next(cd))
# print(next(cd))    # StopIteration


# memory efficiency: list vs generator
import sys


def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

print(sum(firstn(1000000)))
print(sys.getsizeof(firstn(1000000)), "bytes")


def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1

print(sum(firstn_generator(1000000)))
print(sys.getsizeof(firstn_generator(1000000)), "bytes")


# Fibonacci generator
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

fib = fibonacci(30)
for i in fib:
    print(i)

# generator expression
mygenerator = (i for i in range(10) if i % 2 == 0)
for i in mygenerator:
    print(i)

mylist = [i for i in range(10) if i % 2 == 0]
print(mylist)

mygenerator = (i for i in range(10) if i % 2 == 0)
print(list(mygenerator))

mygenerator = (i for i in range(1000000) if i % 2 == 0)
mylist = [i for i in range(1000000) if i % 2 == 0]
print(sys.getsizeof(mygenerator))
print(sys.getsizeof(mylist))