p = (4, 5)
a, b = p
print(a, b)

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, (year, mon, day) = data
print(name, shares, price, year, mon, day)

# if you want to discard some specific values
_, shares, price, _ = data
print(shares, price)


def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)


def avg(seq):
    return float(sum(seq)) / len(seq)


print(drop_first_last([87, 85, 88, 89, 76, 97, 91, 78]))

# phone_numbers will always be a list
records = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = records
print(phone_numbers)
records = ('Dave', 'dave@example.com')
name, email, *phone_numbers = records
print(phone_numbers)
records = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, *_, (*_, year) = records
print(name, year)


def get_sum(items):
    head, *tail = items
    return head + get_sum(tail) if tail else head


print(get_sum([1, 2, 3, 4, 5]))

records = [
    ('fool', 1, 2),
    ('bar', 'hello'),
    ('fool', 3, 4)
]


def do_fool(x, y):
    print('fool', x, y)


def do_bar(s):
    print('bar', s)


for tag, *args in records:
    if tag == 'fool':
        do_fool(*args)
    elif tag == 'bar':
        do_bar(*args)
