n = int(input())

dp = [[0] * 3 for _ in range(n + 1)]

empty = 0
left = 1
right = 2

dp[1][0] = 1
dp[1][left] = 1
dp[1][right] = 1

for i in range(2, n + 1):
    dp[i][left] = dp[i - 1][right] + dp[i - 1][empty]
    dp[i][right] = dp[i - 1][left] + dp[i - 1][empty]
    dp[i][empty] = dp[i - 1][empty] + dp[i - 1][left] + dp[i - 1][right]
    for j in range(3):
        dp[i][j] %= 9901

print(sum(dp[-1]) % 9901)

