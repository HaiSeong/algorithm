
n = int(input())

# 현이가 학생을 부를 수 있는 경우의 수 -> dp[i][0] 번 째 줄이 현이를 부르지 않은 경우,  dp[i][1] 번 째 줄이 현이를 부른 경우
dp = [[0, 0] for _ in range(n + 1)]
dp[1][0] = 2
dp[1][1] = 1
# dp[2][0] = dp[1][1] * 2 + dp[1][0] * 2
# dp[2][1] = dp[1][0]

for i in range(2, n + 1):
    dp[i][0] = 2 * sum(dp[i - 1]) % (10**9 + 7)
    dp[i][1] = dp[i - 1][0] % (10**9 + 7)

print(sum(dp[-1]) % (10**9 + 7))