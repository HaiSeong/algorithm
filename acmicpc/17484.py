n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dirs = [-1, 0, 1]
# dp[i][j][dir] : i, j 로 오기위한 최소 연료, 그런데 마지막으로 dir 방향에서 날아온
dp = [[[float('inf')] * 3 for _ in range(m)] for _ in range(n)]

for j in range(m):
    for k in range(3):
        dp[0][j][k] = graph[0][j]

for i in range(1, n):
    for j in range(m):
        for before_dir in range(3):
            for dir in range(3):
                if before_dir == dir:
                    continue
                if 0 <= j + dirs[dir] < m:
                    dp[i][j][dir] = min(dp[i][j][dir], dp[i - 1][j + dirs[dir]][before_dir] + graph[i][j])

answer = float('inf')
for d in dp[n - 1]:
    answer = min(answer, min(d))
print(answer)
