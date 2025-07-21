
# dp[x] = min(dp[x//5] + 1,dp[x//3] + 1,dp[x//2] + 1,dp[x-1] + 1)

dp = [0] * 30_001

for i in range(2, 30_001):
    cases = [n for n in [5, 3, 2] if i % n == 0]
    dp[i] = min([dp[i // case] + 1 for case in cases] + [dp[i - 1] + 1])

print(dp[int(input())])
