n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

# dp[i][j][k] : i 번째 까지의 최소 합 j를 색칠한 처음에는 k를 색칠했음
dp = [[[float('inf')] * 3 for _ in range(3)] for _ in range(n)]

for i in range(3):
    dp[0][i][i] = graph[0][i]
for i in range(1, n):
    for now in range(3):
        for before in range(3):
            for first in range(3):
                if now == before:
                    continue
                if i == n - 1:
                    if now == first:
                        continue
                dp[i][now][first] = min(dp[i - 1][before][first] + graph[i][now], dp[i][now][first])

print(min(map(min, dp[-1])))