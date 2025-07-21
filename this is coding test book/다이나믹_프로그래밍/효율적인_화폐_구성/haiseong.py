
n, m = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [float("inf")] * 10_001
dp[0] = 0

for i in range(2, 10_001):
    cases = [coin for coin in coins if i - coin >= 0]
    if cases:
        dp[i] = min([dp[i - case] + 1 for case in cases])

answer = dp[m]
if answer == float("inf"):
    answer = -1
print(answer)
