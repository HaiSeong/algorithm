from collections import deque

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]


def move_one(y, x, dir, graph, visited):
    one = graph[y][x]
    graph[y][x] = 0
    dy, dx = dir
    while 0 <= y + dy < n and 0 <= x + dx < n and graph[y + dy][x + dx] == 0:
        y += dy
        x += dx
    if 0 <= y + dy < n and 0 <= x + dx < n:
        if graph[y + dy][x + dx] == one and not visited[y + dy][x + dx]:
            graph[y + dy][x + dx] += one
            visited[y + dy][x + dx] = True
        else:
            graph[y][x] = one
    else:  # 끝 도달
        graph[y][x] = one


def move(dir, graph):
    visited = [[False] * n for _ in range(n)]
    orders = [i for i in range(n)]
    if sum(dir) == 1:
        orders = [i for i in range(n - 1, -1, -1)]

    if dir[0] == 0:
        for i in range(n):
            for j in orders:
                move_one(i, j, dir, graph, visited)
    else:
        for j in range(n):
            for i in orders:
                move_one(i, j, dir, graph, visited)
    # for g in graph:
    #     print(g)

    return graph


answer = 0
queue = deque([graph])
for i in range(5):
    tmp = deque()
    while queue:
        now = queue.popleft()

        for dir in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next = move(dir, [g[:] for g in now])
            for ne in next:
                answer = max(max(ne), answer)

            tmp.append(next)

    queue = tmp

# move((0, 1), graph)
# move((1, 0), graph)
# move((0, 1), graph)
# move((-1,0), graph)
# move((0, 1), graph)

print(answer)

