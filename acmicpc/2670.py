
n = int(input())
lst = [float(input()) for _ in range(n)]

# dp[i] : i 까지 최대
# dp[i] = dp[i - 1] * lst[i]
dp = [[0] * 2 for _ in range(n)]
dp[0][0] = lst[0]
dp[0][1] = lst[0]

for i in range(1, n):
    dp[i][0] = max(dp[i-1][0], dp[i-1][1], lst[i])
    dp[i][1] = max(dp[i-1][1] * lst[i], lst[i])

answer = max(dp[-1])
# print(dp[-1])

print("%.3f" %answer)
