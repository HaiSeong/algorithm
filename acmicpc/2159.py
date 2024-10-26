import sys

input = sys.stdin.readline

n = int(input())
people = [tuple(map(int, input().split())) for _ in range(n + 1)]

# dp[i][j] : i 번째 사람에게 배달하는 최소 거리, 근데 j 번째 방향에서 배달함
dir = [(0, 0), (-1, 0), (0, -1), (1, 0), (0, 1)]

dp = [[float('inf')] * 5 for _ in range(n + 1)]
dp[0][0] = 0
for i in range(1, 5):
    dp[0][i] = 1

for i in range(1, n + 1):
    for j in range(5):
        dy2, dx2 = dir[j]
        y2 = people[i - 1][0] + dy2
        x2 = people[i - 1][1] + dx2
        for k in range(5):
            dy1, dx1 = dir[k]
            y1 = people[i][0] + dy1
            x1 = people[i][1] + dx1

            dist = abs(x1 - x2) + abs(y1 - y2)
            dp[i][j] = min(dp[i][j], dp[i - 1][k] + dist)

print(min(dp[-1]))


