import sys

sys.setrecursionlimit(100000)

# dp[n] : n원에 낼수있는 최소 동전 갯수
n = int(input())

dp = [float('inf')] * (n + 1)


def count(n):
    if n < 0:
        return float('inf')

    if dp[n] < float('inf'):
        return dp[n]

    if n == 0:
        return 0

    dp[n] = min(dp[n], count(n - 2) + 1, count(n - 5) + 1)

    return dp[n]


ans = count(n)
if ans == float('inf'):
    ans = -1
print(ans)
