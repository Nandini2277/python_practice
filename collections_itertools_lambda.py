# COLLECTIONS
from collections import Counter

a = "aaaaabbbbcccc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())

print(my_counter.most_common(1))
print(my_counter.most_common(2))
print(my_counter.most_common(1)[0])
print(my_counter.most_common(1)[0][0])

print(list(my_counter.elements()))

# namedtuple
from collections import namedtuple

Point = namedtuple("Point", "x, y")
pt = Point(1, -4)
print(pt)
print(pt.x, pt.y)

# OrderedDict
from collections import OrderedDict

ordered_dict = OrderedDict()
ordered_dict["b"] = 2
ordered_dict["c"] = 3
ordered_dict["d"] = 4
ordered_dict["a"] = 1
print(ordered_dict)

# defaultdict
from collections import defaultdict

d = defaultdict(int)
d["a"] = 1
d["b"] = 2
print(d)
print(d["a"])
print(d["b"])
print(d["c"])     

d = defaultdict(float)
d["a"] = 1
d["b"] = 2
print(d["c"])      

d = defaultdict(list)
d["a"] = 1
d["b"] = 2
print(d["c"])      

# deque
from collections import deque

d = deque()
d.append(1)
d.append(2)
print(d)
d.appendleft(3)
print(d)
d.pop()
print(d)
d.popleft()
print(d)
d.clear()
d.extend([4, 5, 6])
print(d)
d.extendleft([4, 5, 6])
print(d)
d.rotate(1)
print(d)
d.rotate(2)
print(d)
d.rotate(-1)
print(d)

# ITERTOOLS
from itertools import product

a = [1, 2]
b = [3, 4]
prod = product(a, b)
print(list(prod))

a = [1, 2]
b = [3]
prod = product(a, b, repeat=2)
print(list(prod))

from itertools import permutations

a = [1, 2, 3]
perm = permutations(a)
print(list(perm))
perm = permutations(a, 2)
print(list(perm))

from itertools import combinations, combinations_with_replacement

a = [1, 2, 3, 4]
comb = combinations(a, 2)
print(list(comb))
comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))

from itertools import accumulate
import operator

a = [1, 2, 3, 4]
acc = accumulate(a)
print(a)
print(list(acc))

acc = accumulate(a, func=operator.mul)
print(a)
print(list(acc))

a = [1, 2, 5, 3, 4]
acc = accumulate(a, func=max)
print(a)
print(list(acc))

from itertools import groupby


def smaller_than_3(x):
    return x < 3

a = [1, 2, 3, 4]
group_obj = groupby(a, key=smaller_than_3)
for key, value in group_obj:
    print(key, list(value))

group_obj = groupby(a, key=lambda x: x < 3)
for key, value in group_obj:
    print(key, list(value))

persons = [
    {"name": "Tim", "age": 25},
    {"name": "Dan", "age": 25},
    {"name": "Lisa", "age": 27},
    {"name": "Claire", "age": 28},
]
group_obj = groupby(persons, key=lambda x: x["age"])
for key, value in group_obj:
    print(key, list(value))

# infinite iterators
from itertools import count, cycle, repeat

for i in count(10):
    print(i)
    if i == 15:
        break

a = [1, 2, 3]
for i in cycle(a):
    print(i)       # infinite - stop with Ctrl+C

for i in repeat(1, 4):
    print(i)

# LAMBDA
add10 = lambda x: x + 10
print(add10(5))                 


def add10_func(x):
    return x + 10

print(add10_func(5))

mult = lambda x, y: x * y
print(mult(2, 7))               

# sorted with key
points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D)
print(points2D)
print(points2D_sorted)

points2D_sorted = sorted(points2D, key=lambda x: x[1])
print(points2D_sorted)

points2D_sorted = sorted(points2D, key=lambda x: x[0] + x[1])
print(points2D_sorted)

# map
a = [1, 2, 3, 4, 5]
b = map(lambda x: x * 2, a)
print(list(b))
c = [x * 2 for x in a]
print(c)

# filter
a = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x % 2 == 0, a)
print(list(b))
c = [x for x in a if x % 2 == 0]
print(c)

# reduce
from functools import reduce

a = [1, 2, 3, 4]
product_a = reduce(lambda x, y: x * y, a)
print(product_a)    
