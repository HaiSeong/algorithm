n = int(input())
finding = int(input())

graph = [[0] * (n + 2) for _ in range(n + 2)]

sy, sx = (n + 1) // 2, (n + 1) // 2

num = 1
for i in range(sy, 0, -1):
    graph[i][i] = num * num

    for j in range(1, num):
        graph[i + j][i] = graph[i + j - 1][i] - 1

    for j in range(1, num):
        graph[i + num - 1][i + j] = graph[i + num - 1][i + j - 1] - 1

    for j in range(1, num):
        graph[i + num - 1 - j][i + num - 1] = graph[i + num - 1 - j + 1][i + num - 1] - 1

    for j in range(1, num - 1):
        graph[i][i + num - 1 - j] = graph[i][i + num - 1 - j + 1] - 1

    num += 2

answer = 0

for i, g in enumerate(graph):
    if finding in g:
        answer = (i, g.index(finding))
    if i != 0 and i != len(g) - 1:
        print(*g[1:-1])

print(*answer)
