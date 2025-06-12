def maxBridgesRec(a, b, i, j):
    if i == len(a) or j == len(b):
        return 0

    if a[i] == b[j]:
        return 1 + maxBridgesRec(a, b, i + 1, j + 1)
    else:
        return max(maxBridgesRec(a, b, i + 1, j), maxBridgesRec(a, b, i, j + 1))

def maxBridges(a, b):
    return maxBridgesRec(a, b, 0, 0)

# Example usage
n = 4
m = 5
a = [1, 1, 2, 1]
b = [1, 2, 1, 2, 1]
print(maxBridges(a, b))