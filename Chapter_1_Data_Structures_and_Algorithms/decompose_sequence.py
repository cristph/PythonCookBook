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


