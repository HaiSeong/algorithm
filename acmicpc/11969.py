
n, q = map(int, input().split())

cows = [0] + [int(input()) for _ in range(n)]

queries = [tuple(map(int, input().split())) for _ in range(q)]
dp = [[0] * 4 for _ in range(n + 1)] # dp[i][j] : 0 ~ i 번째 까지 j 종류의 소 갯수

dp[0][cows[0]]

for i in range(1, n + 1):
    for j in range(1, 4):
        dp[i][j] = dp[i - 1][j]
    cow = cows[i]
    dp[i][cow] += 1

for start, end in queries:
    print(dp[end][1] - dp[start - 1][1], dp[end][2] - dp[start - 1][2], dp[end][3] - dp[start - 1][3])


