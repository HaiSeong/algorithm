import heapq
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]
dp[0][0] = 1

heap = []
for i in range(n):
    for j in range(m):
        heapq.heappush(heap, (-graph[i][j], i, j))

answer = 0

while heap:
    _, y, x = heapq.heappop(heap)

    for dy, dx in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
        ny = dy + y
        nx = dx + x
        if 0 <= ny < n and 0 <= nx < m:
            if graph[y][x] < graph[ny][nx]:
                dp[y][x] += dp[ny][nx]

print(dp[n - 1][m - 1])

