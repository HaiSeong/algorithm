import sys

input = sys.stdin.readline

n = int(input())
lst = [int(input()) for _ in range(n)]

dp = [1] * n
for i in range(1, n):
    for j in range(i):
        if lst[i] > lst[j]:
            dp[i] = max(dp[j] + 1, dp[i])

print(n - max(dp))
