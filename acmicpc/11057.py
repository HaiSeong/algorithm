div = 10007
n = int(input())

# dp[i][j] : 길이가 i, 마지막 수가 j 인 수의 경우의 수
# dp
dp = [[0] * 10 for _ in range(n + 1)]

for j in range(10):
    dp[1][j] = 1

for i in range(2, n + 1):
    for j in range(10):
        for k in range(j, 10):
            dp[i][j] += dp[i - 1][k] % div

print(sum(dp[n]) % div)


