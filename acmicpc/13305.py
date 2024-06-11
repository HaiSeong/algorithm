
n = int(input())
distances = list(map(int, input().split()))
costs = list(map(int, input().split()))

# dp[i] : i 까지 가기위한 최소 비용
dp = [float('inf')] * n
dp[0] = 0
cheapest_cost = costs[0]
for i in range(1, n):
    cheapest_cost = min(costs[i - 1], cheapest_cost)
    dp[i] = dp[i - 1] + cheapest_cost * distances[i - 1]

print(dp[n - 1])