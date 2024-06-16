import sys

input = sys.stdin.readline

n, t = map(int, input().split())
costs, fees = [], []
for _ in range(n):
    c, f = map(int, input().split())
    costs.append(c)
    fees.append(f)

# dp[i][j] = j만큼의 기간을 사용하면서 i번 문제를 고려한경우 최대로 깎은 벌금
# dp[i][j] = dp[i-1][j] or dp[i-1][j-costs[i]] + fees[i]
dp = [[0] * (t + 1) for _ in range(n)]

for j in range(costs[0], t+1):
    dp[0][j] = fees[0]

for i in range(1, n):
    for j in range(1, t+1):
        dp[i][j] = dp[i-1][j]
        if j - costs[i] >= 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j-costs[i]] + fees[i])

result = 0
for d in dp:
    result = max(result, max(d))

answer = sum(fees) - result
print(answer)
