import sys

input = sys.stdin.readline

n = int(input())
t = []
p = []
finish = [[] for _ in range(n + 1)]
for i in range(n):
    t_, p_ = map(int, input().split())
    t.append(t_)
    p.append(p_)
    fin = i + t_
    if fin < n + 1:
        finish[fin].append(i)
t.append(0)
p.append(0)

k = max(t)
# dp[i] : i 번째 날에 최대 벌 수 있는 돈
# dp[i] = max(p[f] + dp[f], ... )
dp = [0] * (n + 1)
dp[0] = 0

for i in range(n + 1):
    dp[i] = dp[i - 1]
    for f in finish[i]:
        dp[i] = max(dp[i], dp[f] + p[f])

print(max(dp))
