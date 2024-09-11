div = 10**9 + 7

n, k = map(int, input().split())
essentials = list(map(int, input().split()))

# dp[i][j] : i번 수업을 고려한 경우의 수, i번째 수업을 고려하고 나서 j 연강임
dp = [[0] * (k + 1) for _ in range(n)]
dp[0][0] = (essentials[0] + 1) % 2
dp[0][1] = 1

for i in range(1, n):
    for j in range(1, k+1):
        dp[i][j] = dp[i - 1][j - 1] % div

    if essentials[i] == 0:
        dp[i][0] = sum(dp[i - 1]) % div

# print(dp)
# print(sum(dp[n - 1]))

dp2 = [[0] * (k) for _ in range(n)]
dp2[0][0] = (essentials[0] + 1) % 2
if k > 1:
    dp2[0][1] = 1

for i in range(1, n):
    for j in range(1, k):
        dp2[i][j] = dp2[i - 1][j - 1] % div

    if essentials[i] == 0:
        dp2[i][0] = sum(dp2[i - 1]) % div

# print(dp2)
# print(sum(dp2[n - 1]))

print((sum(dp[n - 1]) - sum(dp2[n - 1])) % div)