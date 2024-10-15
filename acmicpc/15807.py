import sys

input = sys.stdin.readline

n = int(input())
lights = []
for _ in range(n):
    x, y = map(int, input().split())
    lights.append((y + 1500, x + 1500))
m = int(input())
poses = []
for _ in range(m):
    x, y = map(int, input().split())
    poses.append((y + 1500, x + 1500))

# dp[i][j] : i, j 에서의 빛의 세기
dp = [[0] * 3002 for _ in range(3002)]

for y, x in lights:
    i, j = y, x
    while 0 <= i <= 3001 and 0 <= j <= 3001:
        dp[i][j] += 1
        i += 1
        j += 1
    i, j = y + 1, x - 1
    while 0 <= i <= 3001 and 0 <= j <= 3001:
        dp[i][j] += 1
        i += 1
        j -= 1

for x in range(3002):
    for y in range(1, 3002):
        dp[y][x] += dp[y - 1][x]

for y, x in poses:
    print(dp[y][x])

