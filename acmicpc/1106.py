c, n = map(int, input().split())

cost = []
people = []
for _ in range(n):
    c_, p_ = map(int, input().split())
    cost.append(c_)
    people.append(p_)

# dp[i] : i명의 사람을 얻기 위해 필요한 최소 금액
# p : people
# dp[i] = dp[i-people[j]] + c[j]

bound = max([((c // p) + 1) * p for p in people])

dp = [float('inf')] * (bound + 1)
dp[0] = 0

i = 0
for i in range(bound + 1):
    for j in range(n):
        p = i - people[j]
        if p >= 0:
            dp[i] = min(dp[i], dp[p] + cost[j])

# print(dp)

print(min(dp[c:]))
