import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0] * (n + 1)] +[[0] + list(map(int, input().split())) for _ in range(n)]

#   [ 1 2 3 4]
#   [ 2 2 3 4]
#   [ 3 2 3 4]
#   [ 4 2 3 4]

# dp[i][j] : (0, 0)에서 (i, j) 까지의 합
# dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + graph[i][j]
dp =  [[0] * (n + 1) for _ in range(n+1)]
dp[1][1] = graph[1][1]
for i in range(1, n+1):
    dp[1][i] = graph[1][i] + dp[1][i - 1]
    dp[i][1] = graph[i][1] + dp[i - 1][1]

for i in range(2, n + 1):
    for j in range(2, n + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + graph[i][j]

for _ in range(m):
    sy, sx, ey, ex = map(int, input().split())
    sy -= 1
    sx -= 1
    print(dp[ey][ex] - dp[sy][ex] - dp[ey][sx] + dp[sy][sx])
