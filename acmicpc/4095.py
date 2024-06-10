while True:
    n, m = map(int, input().split())

    if n == 0 and m == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(n)]

    dp = [g[:] for g in graph]

    for i in range(1, n):
        for j in range(1, m):
            if graph[i][j] == 1:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

    answer = 0
    for d in dp:
        answer = max(answer, max(d))
    print(answer)