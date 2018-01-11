import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

# use heapq to get top k when k is small
cheap = heapq.nsmallest(3, portfolio, lambda p: p['price'])
expensive = heapq.nlargest(3, portfolio, lambda p: p['price'])
print('top3 cheap', cheap)
print('top3 expensive', expensive)

# when want to find min or max, please use
most_cheap = min(portfolio, key=lambda p: p['price'])
most_expensive = max(portfolio, key=lambda p: p['price'])
print(most_cheap, most_expensive)

# when k is near to len(list), please use
cheap = sorted(portfolio, key=lambda p: p['price'])[:5]
expensive = sorted(portfolio, key=lambda p: p['price'])[-5:]
print('top5 cheap', cheap)
print('top5 expensive', expensive)
expensive = sorted(portfolio, key=lambda p: p['price'], reverse=True)[:5]
print('top5 expensive', expensive)

heapq.heapify(nums)
print(nums)
print(type(nums))
print(heapq.heappop(nums))
print(nums)
print(heapq.heappop(nums))
print(nums)

# Pop and return the current smallest value, and add the new item.
print(heapq.heapreplace(nums, 3))
print(nums)

# Fast version of a heappush followed by a heappop.
print(heapq.heappushpop(nums, 5))
print(nums)
