
n,m =map(int, input().split())
lst = [tuple(map(int, input().split())) for _ in range(n)]

# dp[i][j] i번째 배낭을 고려했는데 j 만큼 무게를 쓴거의 가치 최대값

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(n):
    w, v = lst[i]
    for j in range(m + 1):
        dp[i + 1][j] = dp[i][j]
        if j - w >= 0:
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j - w] + v)
    # print(dp[i + 1])

print(max(dp[-1]))
