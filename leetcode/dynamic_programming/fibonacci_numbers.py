from functools import cache


def fib(n: int) -> int:
    if n <= 1:
        return n
    return fib(n - 2) + fib(n - 1)


def topdown_fib(n: int, dp: dict) -> int:
    if n <= 1:
        return n
    if n in dp:
        return dp[n]

    dp[n] = topdown_fib(n - 1, dp) + topdown_fib(n - 2, dp)
    return dp[n]


def bottomup_fib(n: int) -> int:
    if n < 2:
        return n

    dp = [0, 1]
    i = 2
    while i <= n:
        tmp = dp[1]
        dp[1] = dp[0] + dp[1]
        dp[0] = tmp
        i += 1
    return dp[1]


print(fib(10))
print(topdown_fib(10, {}))
print(bottomup_fib(10))
