# dp[0] = lst[0]
# dp[1] = max(lst[0], lst[1])
# dp[2] = max(lst[0] + lst[2], lst[1])
# dp[n] = max(dp[n-2] + lst[n], dp[n-1])

n = int(input())
dp = [0] * n
lst = list(map(int, input().split()))

dp[0] = lst[0]
dp[1] = max(lst[0], lst[1])
for i in range(2, n):
    dp[i] = max(dp[i - 2] + lst[i], dp[i - 1])

print(dp[-1])
