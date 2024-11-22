
n, m = map(int, input().split())

graph = []

for _ in range(3 * n):
    graph.append(list(input()))

for y in range(n):
    for x in range(m):
        i = y * 3
        j = x * 8
        a = int(graph[i + 1][j + 1])
        b = int(graph[i + 1][j + 1 + 2])
        c = int(graph[i + 1][j + 1 + 2 + 2])

        flag = False
        if graph[i + 1][j + 1 + 2 + 3] != '.':
            c = 10 * c + int(graph[i + 1][j + 1 + 2 + 3])
            flag = True

        if a + b == c:
            graph[i + 1][j] = '*'
            jj = j + 1
            while graph[i + 1][jj] != '.':
                graph[i][jj] = '*'
                graph[i + 2][jj] = '*'
                jj+=1
            graph[i + 1][jj] = '*'
        else:
            graph[i][j + 3] = '/'
            graph[i + 1][j + 2] = '/'
            graph[i + 2][j + 1] = '/'


for g in graph:
    print(''.join(g))