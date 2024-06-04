import timeit


# time: O(2^n), space: O(n) for n recursive stack
def brute_force(profit, weight, capacity):
    def dfs(i, capacity):
        if i == len(profit):
            return 0

        # not choose i
        not_choose_profit = dfs(i + 1, capacity)

        # choose i
        choose_profit = 0
        if capacity - weight[i] >= 0:
            choose_profit = dfs(i + 1, capacity - weight[i]) + profit[i]

        return max(not_choose_profit, choose_profit)

    return dfs(0, capacity)


# time: O(n * m), space: O(n * m)
def memorization(profit, weight, capacity):
    # two variables: current position i and current capacity
    N, M = len(profit), capacity
    dp = [[-1] * (M + 1) for _ in range(N)]  # [i][capacity]

    def dfs(i, capacity):
        if i == len(profit):
            return 0

        if dp[i][capacity] != -1:
            return dp[i][capacity]

        # not choose i
        not_choose_profit = dfs(i + 1, capacity)

        # choose i
        choose_profit = 0
        if capacity - weight[i] >= 0:
            choose_profit = dfs(i + 1, capacity - weight[i]) + profit[i]

        dp[i][capacity] = max(not_choose_profit, choose_profit)
        return dp[i][capacity]

    return dfs(0, capacity)


# Time: O(n * m), Space: O(n * m)
def bottom_up_dp(profit, weight, capacity):
    N, M = len(profit), capacity
    dp = [[0] * (M + 1) for _ in range(N)]  # [item][capacity]

    # Fill the first column and row to reduce edge cases
    for i in range(N):
        dp[i][0] = 0
    for c in range(M + 1):
        if weight[0] <= c:
            dp[0][c] = profit[0]

    for i in range(1, N):
        for c in range(1, M + 1):
            skip = dp[i-1][c]
            include = 0
            if c - weight[i] >= 0:
                include = profit[i] + dp[i-1][c - weight[i]]
            dp[i][c] = max(include, skip)
    return dp[N-1][M]


# Time: O(n * m), Space: O(m)
def buttom_up_dp_memory_optimization(profit, weight, capacity):
    N, M = len(profit), capacity
    dp = [0] * (M + 1)  # [capacity]

    # Fill the first row to reduce edge cases
    for c in range(M + 1):
        if weight[0] <= c:
            dp[0] = profit[0]

    for i in range(1, N):
        curRow = [0] * (M + 1)
        for c in range(1, M + 1):
            skip = dp[c]
            include = 0
            if c - weight[i] >= 0:
                include = profit[i] + dp[c - weight[i]]
            curRow[c] = max(include, skip)
        dp = curRow
    return dp[M]


capacity = 8
profit = [4, 4, 7, 1]
weight = [5, 2, 3, 1]

print(brute_force(profit, weight, capacity))
print(memorization(profit, weight, capacity))
print(bottom_up_dp(profit, weight, capacity))
print(buttom_up_dp_memory_optimization(profit, weight, capacity))
