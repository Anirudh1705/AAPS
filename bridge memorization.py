def maxBridges(a, b):
    from functools import lru_cache
    n, m = len(a), len(b)
    @lru_cache(maxsize=None)
    def helper(i, j):
        if i == n or j == m:
            return 0
        if a[i] == b[j]:
            return 1 + helper(i + 1, j + 1)
        else:
            return max(helper(i + 1, j), helper(i, j + 1))

    return helper(0, 0)

# Example usage
n = 4
m = 5
a = [1, 1, 2, 1]
b = [1, 2, 1, 2, 1]
print(maxBridges(a, b))