import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())
candies = [0] + list(map(int, input().split()))
graph = [set() for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

visited = [0] * (n + 1)

costs = []
weights = []
queue = deque()


def bfs(start):
    queue.append(start)
    visited[start] = True

    cnt_kid = 0
    cnt_candies = 0

    while queue:
        now = queue.popleft()

        cnt_kid += 1
        cnt_candies += candies[now]

        for next in graph[now]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)

    weights.append(cnt_kid)
    costs.append(cnt_candies)


for kid in range(1, n + 1):
    if not visited[kid]:
        bfs(kid)

length = len(costs)
dp = [[0] * k for _ in range(length)]
# dp[i][j] i번째 아이들의 사탕을 뻈을지 말지 고려한, j명을 울리고 제한으로, 최고 사탕 수

for j in range(weights[0], k):
    dp[0][j] = costs[0]

for i in range(1, length):
    for j in range(k):
        dp[i][j] = dp[i - 1][j]
        if j - weights[i] >= 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - weights[i]] + costs[i])

print(max(dp[-1]))