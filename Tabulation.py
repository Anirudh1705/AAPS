def fun(coins, target):
    n = len(coins)
    table = [[0] * (target + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        table[i][0] = 1
    for i in range(1, n + 1):
        for j in range(target + 1):
            if coins[i - 1] <= j:
                table[i][j] = table[i][j - coins[i - 1]] + table[i - 1][j]
            else:
                table[i][j] = table[i - 1][j]
    return table[n][target]
print(fun([1, 3, 6], 855568))
