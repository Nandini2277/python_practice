# Python Practice

This repository holds my code-along practice files from learning Python through YouTube tutorials. Each file contains the code I typed and experimented with while following video tutotirals, and includes lots of small examples, comments, and print statements rather than polished programs.

## Videos I followed

I worked through three videos, in this order. 
The first is a Python basics tutorial (https://www.youtube.com/watch?v=eWRfhZUzrAc). 
The second is an intermediate Python tutorial (https://www.youtube.com/watch?v=HGOBQPFzWKo).
The third is a course on object-oriented programming (OOP) in Python (https://www.youtube.com/watch?v=Ej_02ICOIgs).

## What's in this repo
### 1. Python basics

python_core_concepts.py:
my notes file for the whole basics video. It walks through variables, data types, arithmetic, comparison and boolean operators, the ternary operator, strings and their methods, slicing, truthiness, numbers, enums, user input, control statements, lists, sorting, tuples, dictionaries, and sets. It then moves on to functions (including how parameters are passed, return values, variable scope, nested functions, and closures), loops with break and continue, a first look at classes, and how to split code into modules.

rockPaperScissor.py:
a small command-line game. You type rock, paper, or scissors, the computer picks one at random using random.choice, and a function decides who wins and prints a message.

blackjack.py:
a larger practice project, a text-based blackjack game built with classes. A Card holds a suit and rank, a Deck builds all 52 cards and can shuffle and deal them, a Hand adds up card values (counting aces as 1 or 11) and checks for blackjack, and a Game class runs the rounds and decides the winner. Running the file starts a game straight away.

### 2. Intermediate Python

lists_tuples_dicts_sets_strings.py:
goes deep on the built-in data structures. For lists it covers indexing, slicing, copying, and list comprehensions. For tuples it covers immutability, unpacking, and how they compare with lists in size and speed. Dictionaries cover copying, merging with update, and what can be used as a key. Sets include frozenset, and strings cover immutability, why join beats +=, and formatting including f-strings.

collections_itertools_lambda.py:
practices the collections module (Counter, namedtuple, OrderedDict, defaultdict, and deque), then itertools (product, permutations, combinations, accumulate, groupby, and the infinite iterators count, cycle, and repeat), and finally lambda functions with sorted, map, filter, and reduce.

exceptions_logging_json_random.py:
covers four topics. The exceptions section lists the common error types, then uses raise, assert, try/except/else/finally, and custom exception classes. The logging section covers log levels, using a logger per module, handlers, a config file, capturing tracebacks, and rotating log files. The JSON section covers reading and writing JSON, including a custom encoder, and the random section covers the random module, secrets, and NumPy's random functions.

decorators_generators.py:
starts with decorators a basic one, a reusable template, decorators that take arguments, nested decorators, and a class-based decorator that counts calls. It then covers generators using yield, next(), a countdown, a memory comparison against lists, a Fibonacci generator, and generator expressions.

arguments_asterisk_copying_contextmanagers.py:
covers four topics. The first is function arguments: positional, keyword, default, *args, **kwargs, keyword-only arguments, local versus global variables, and how arguments are passed. The second is the * operator for multiplication, repeating, and unpacking. The third is shallow versus deep copying with the copy module. The last is context managers, written both as a class with __enter__ and __exit__ and with @contextmanager.

Threading

basicThreading.py:
creates ten threads that each run the same function, starts them all, and waits for them with join() before printing "end main".

threadsRacenLock.py:
shows a race condition. Two threads read, change, and write back a shared value, and a Lock keeps the result correct. The comment at the bottom notes that without the lock the final value is 1 instead of 2.

threadDaemon.py:
uses a Queue with ten daemon worker threads. The workers pull numbers from the queue and print them while holding a lock, and the main thread waits with q.join(). Because the workers are daemons, they stop when the main program ends.

Multiprocessing

basicMultiprocessing.py:
starts one process per CPU core, each running the same function, then joins them all. It includes the if __name__ == "__main__": guard that multiprocessing needs on Windows and macOS.

mpSharedVal.py:
has two processes increment one shared Value while a lock keeps the count correct. mpSharedArr.py does the same with a shared Array of three numbers.

mpQueue.py:
has two processes put results on a shared Queue, one squaring the numbers and one making them negative, and the main process then prints everything from the queue.

mpPool.py:
uses a Pool to cube the numbers 0 to 9 with map, spreading the work across the CPU cores, and also shows apply for a single call.

### 3. Object-oriented programming (OOP)

These files together form one small store management system that I built step by step while following the OOP video.

item.py:
The main Item class. It demonstrates the constructor with assert validation, instance attributes versus class attributes (pay_rate and all), __repr__, a class method (instantiate_from_csv), and a static method (is_integer). It also has a private name and price exposed through @property with a setter that rejects names longer than ten characters, apply_discount, apply_increment, and calculate_total_price. The private email-sending methods behind send_email show abstraction.

phone.py:
defines Phone, a child class of Item that adds a broken_phones attribute and calls super().__init__() to reuse the parent's setup.

keyboard.py:
defines Keyboard, another child class of Item. It overrides pay_rate to 0.7, so keyboards get a 30% discount while other items get 20%, which shows polymorphism.

items.csv:
holds sample store data (name, price, and quantity) that Item.instantiate_from_csv() reads to create the item objects.

main.py:
imports the classes and tries everything out: loading items from the CSV, the static method, a phone, the name setter, price increments and discounts, and the keyboard discount.

## How to run

Install Python 3, then clone the repo and move into the folder:

git clone https://github.com/Nandini2277/python_practice.git
cd python_practice

Run any file with python filename.py. For the OOP project, run python main.py from inside the repo folder so that items.csv can be found. The multiprocessing files are best run from a terminal rather than inside some notebooks, and rockPaperScissor.py and blackjack.py wait for keyboard input.