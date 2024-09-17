
n, m = map(int, input().split())

games = [list(map(int, input().split())) for _ in range(n)]

# dp[i][j] : i번째 스테이지에 j 번 무기를 사용하는데 가장 효율적인 시간
dp = [[0] * m for _ in range(n)]
for j in range(m):
    dp[0][j] = games[0][j]

for i in range(1, n):
    for j in range(m):
        dp[i][j] = games[i][j] + min((dp[i - 1][:j] + (dp[i - 1][j + 1:])))

print(min(dp[-1]))