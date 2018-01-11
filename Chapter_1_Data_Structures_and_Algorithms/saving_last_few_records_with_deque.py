from collections import deque

# Deques are a generalization of stacks and queues
# (the name is pronounced “deck” and is short for “double-ended queue”).
# Deques support thread-safe, memory efficient appends and pops from either side
# of the deque with approximately the same O(1) performance in either direction.

# create a deque with the fixed length
q = deque(maxlen=3)
# create a simple queue
q = deque()
q.append(1)
q.appendleft(2)
q.pop()
q.popleft()


# yield
def square():
    for x in range(4):
        yield x ** 2


square_gen = square()
for x in square_gen:
    print(x)

generator = square().__iter__()
while True:
    try:
        x = generator.__next__()
        print(x)
    except StopIteration:
        break


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


# Example use on a file
if __name__ == '__main__':
    with open('test.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)
