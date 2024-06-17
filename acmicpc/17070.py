from collections import deque

RIGHT = 0
DOWN = 1
RIGHT_DOWN = 2

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]
dp[0][1][RIGHT] = 1

for i in range(n):
    for j in range(n):
        if 0 <= i < n and 0 < j < n:
            if graph[i][j] == 0:
                dp[i][j][RIGHT] += dp[i][j - 1][RIGHT]
                dp[i][j][RIGHT] += dp[i][j - 1][RIGHT_DOWN]

        if 0 < i < n and 0 <= j < n:
            if graph[i][j] == 0:
                dp[i][j][DOWN] += dp[i - 1][j][DOWN]
                dp[i][j][DOWN] += dp[i - 1][j][RIGHT_DOWN]

        if 0 < i < n and 0 < j < n:
            if graph[i][j] == 0 and graph[i - 1][j] == 0 and graph[i][j - 1] == 0:
                dp[i][j][RIGHT_DOWN] += dp[i - 1][j - 1][DOWN]
                dp[i][j][RIGHT_DOWN] += dp[i - 1][j - 1][RIGHT]
                dp[i][j][RIGHT_DOWN] += dp[i - 1][j - 1][RIGHT_DOWN]

print(sum(dp[n-1][n-1]))
