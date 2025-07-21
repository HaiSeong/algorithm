# dp[0] = 0
# dp[1] = 1
# dp[2] = 3
# dp[3] = dp[2] + 2 * dp[1]
# dp[n] = dp[n-1] + 2 * dp[n-2]


dp = [0] * 1001
dp[0] = 0
dp[1] = 1
dp[2] = 3

for i in range(3, 1001):
    dp[i] = (dp[i - 1] + 2 * dp[i - 2]) % 796_796

print(dp[int(input())])
