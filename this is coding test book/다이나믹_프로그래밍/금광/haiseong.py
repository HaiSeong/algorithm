
for _ in range(int(input())):
    n, m = map(int, input().split())
    line = list(map(int, input().split()))
    graph = [line[i * m : (i + 1) * m] for i in range(n)]
    dp = [[0] * m for _ in range(n)]
    for i in range(n):
        dp[i][0] = graph[i][0]

    for j in range(1, m):
        for i in range(n):
            dp[i][j] = dp[i][j - 1] + graph[i][j]
            if 0 <= i - 1 < n:
                dp[i][j] = max(dp[i][j], dp[i-1][j - 1] + graph[i][j])
            if 0 <= i + 1 < n:
                dp[i][j] = max(dp[i][j], dp[i+1][j - 1] + graph[i][j])

    answer = max(map(max, dp))
    print(answer)