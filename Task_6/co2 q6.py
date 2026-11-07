from functools import lru_cache
calls = 0
def ways_naive(n):
    global calls
    calls += 1
    if n <= 1:
        return 1
    return ways_naive(n - 1) + ways_naive(n - 2)
@lru_cache(maxsize=None)
def ways_memo(n):
    global calls
    calls += 1
    if n <= 1:
        return 1
    return ways_memo(n - 1) + ways_memo(n - 2)
calls = 0
print("Naive:", ways_naive(25), "calls =", calls)
calls = 0
print("Memo:", ways_memo(25), "calls =", calls)
print("Testing n = 1000")
try:
    print(ways_memo(1000))
except RecursionError:
    print("RecursionError: Maximum recursion depth exceeded")
