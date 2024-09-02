n = int(input())
lst = list(map(int, input().split()))

dp = [[0] * 3 for _ in range(n)]

# dp[i][j] i초에 받는 점수인데 j초만큼 까지 점수 두배 받음
dp[0][0] = lst[0]
dp[0][1] = -float('inf')
dp[0][2] = 2 * lst[0] # dp[1][1] -> dp[2][0]

dp[1][0] = dp[0][0] + lst[1]
dp[1][1] = dp[0][2] + 2 * lst[1]
dp[1][2] = dp[0][0] + 2 * lst[1]

for i in range(2, n):
    dp[i][0] = max(dp[i - 1][0] + lst[i], dp[i - 1][1] + 2 * lst[i])

    dp[i][1] = dp[i - 1][2] + 2 * lst[i]

    dp[i][2] = dp[i - 1][0] + 2 * lst[i]
# for d in dp:
#     print(d)
print(max(dp[-1]))