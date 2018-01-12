from collections import defaultdict
from collections import OrderedDict
import json

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(1)
print(d)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['a'].add(1)
print(d)

d = defaultdict(list)
pairs = [(1, 2), (2, 3), (3, 4)]
for key, value in pairs:
    d[key].append(value)
print(d)

# to control the order of keys in dict
d = OrderedDict()
d['fool'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
for key in d:
    print(key, d[key])
json_str = json.dumps(d)
print(json_str)
d = json.loads(json_str)
print(d)

# calculation on a dict
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# content in zip() can only be consumed once
# operations can only be done on keys on a dict, that's why we need zip()
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(min_price)
print(max_price)
print(prices_sorted)

a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

# keys(), items() support set operations
# while values() not support for that
print(type(a.keys()), a.keys())
print(type(a.items()), a.items())
print(type(a.values()), a.values())

# find keys in common
print(a.keys() & b.keys())

# find keys in a that are not in b
print(a.keys() - b.keys())

# find (key, value) pairs in common
print(a.items() & b.items())

# make a new dictionary with certain keys removed
print({key: a[key] for key in a.keys() - {'z', 'w'}})
