n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
bsy, bsx, bey, bex = map(int, input().split())
if bsy > bey:
    bsy, bey = bey, bsy
if bsx > bex:
    bsx, bex = bex, bsx


next_block = set()
# for g in graph:
#     print(g)

dp = [graph[i][:] for i in range(n)]

if bsy == bey: # 가로벽
    # print("가로")
    for j in range(bsx, bex):
        next_block.add((bsy, j))
    # print(next_block)

    for j in range(1, m):
        dp[0][j] += dp[0][j - 1]

    for i in range(1, n):
        if (i, 0) in next_block:
            dp[i][0] = -float("inf")
        else:
            dp[i][0] += dp[i - 1][0]

    for i in range(1, n):
        for j in range(1, m):
            if (i, j) in next_block:
                dp[i][j] += dp[i][j - 1]
            else:
                dp[i][j] += max(dp[i - 1][j], dp[i][j - 1])
else: # 세로
    # print("세로")
    for i in range(bsy, bey):
        next_block.add((i, bsx))

    for i in range(1, n):
        dp[i][0] += dp[i - 1][0]

    for j in range(1, m):
        if (0, j) in next_block:
            dp[0][j] = -float("inf")
        else:
            dp[0][j] += dp[0][j - 1]

    for i in range(1, n):
        for j in range(1, m):
            if (i, j) in next_block:
                dp[i][j] += dp[i - 1][j]
            else:
                dp[i][j] += max(dp[i - 1][j], dp[i][j - 1])

# for d in dp:
#     print(d)

if dp[-1][-1] == -float("inf"):
    print("Entity")
else:
    print(dp[n - 1][m - 1])