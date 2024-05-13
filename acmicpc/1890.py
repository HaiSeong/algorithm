n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# dp[i][j] : (i,j)로 올 수 있는 경우의 갯수
# dp[i][j] = (graph[i-1][j] == 1) dp[i-1][j] + (graph[i-2][j] == 2) dp[i-2][j] + ...
#           + (graph[i][j-1] == 1) dp[i][j-1] + (graph[i][j-1] == 2) dp[i][j-2] + ...

dp = [[0] * n for _ in range(n)]

dp[0][0] = 1

for i in range(n):
    for j in range(n):
        x = 1
        while i - x >= 0:
            if graph[i - x][j] == x:
                dp[i][j] += dp[i - x][j]
            x+=1
        y = 1
        while j - y >= 0:
            if graph[i][j - y] == y:
                dp[i][j] += dp[i][j - y]
            y+=1

print(dp[n-1][n-1])


