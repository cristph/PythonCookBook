# remove duplicates
# if you don't care about the order of elements
a = [1, 5, 2, 1, 9, 1, 5, 10]
a = set(a)
print(a)


# remove duplicates while maintaining order of the sequence

# when the element in sequence has __hash__(),
# which means doesn't change in lifetime
# such as integer, float, string, tuple, etc.
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
        seen.add(item)


a = [1, 5, 2, 1, 9, 1, 5, 10]
a = list(dedupe(a))
print(a)


# when the element in sequence doesn't have __hash__()
# such as list. dict, etc.
def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

