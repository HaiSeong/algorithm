import heapq

left, right, back, k = map(int, input().split())

dp = [[float('inf')] * 4 for _ in range(k + 1)]
dp[0][0] = 0

for i in range(1, k + 1):
    for j in range(4):
        if 0 <= i - left <= k:
            dp[i][j] = min(dp[i][j], dp[i - left][(j + 1) % 4] + 1)
        if 0 <= i - right <= k:
            dp[i][j] = min(dp[i][j], dp[i - right][(j + 3) % 4] + 1)
        if 0 <= i - back <= k:
            dp[i][j] = min(dp[i][j], dp[i - back][(j + 2) % 4] + 1)

answer = dp[k][0]
if answer == float('inf'):
    answer = -1
print(answer)