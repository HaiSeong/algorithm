n, k = map(int, input().split())
lst = list(map(int, input().split()))

dp = [[0] * (k+1) for _ in range(n)]
# dp[n][k] : k번 건너뛴 n번째 까지 최대 길이
# dp[n][0] = (lst[n]이 짝수면) : dp[n-1][0] + 1
# dp[n][1] = (lst[n]이 짝수면) : dp[n-1][1] + 1
# dp[n][1] = (lst[n]이 홀수면) : dp[n-1][0]
# dp[n][2] = (lst[n]이 짝수면) : dp[n-1][2] + 1
# dp[n][2] = (lst[n]이 홀수면) : dp[n-1][1]
# dp[n][k] = (lst[n]이 짝수면) : dp[n-1][k] + 1
# dp[n][k] = (lst[n]이 홀수면) : dp[n-1][k-1]

for i in range(n):
    for j in range(k+1):
        if lst[i] % 2 == 0:
            dp[i][j] = max(dp[i - 1][j] + 1, dp[i][j])
        elif lst[i] % 2 ==1 and j > 0:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i][j])

answer = 0
for d in dp:
    answer = max(answer, max(d))
print(answer)