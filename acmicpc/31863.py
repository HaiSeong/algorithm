from collections import deque

n, m = map(int, input().split())

graph = [[0] * m for _ in range(n)]

sy, sx = 0, 0
not_broken = 0
broken = 0
for i in range(n):
    for j, type in enumerate(list(input())):
        if type == '@':
            sy, sx = i, j
        elif type == '*':
            graph[i][j] = 1
            not_broken += 1
        elif type == '#':
            graph[i][j] = 2
            not_broken += 1
        elif type == '|':
            graph[i][j] = -1

queue = deque([(sy, sx, True)])

while queue:
    y, x, first = queue.popleft()

    dist = 1
    if first:
        dist = 2
    for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        for i in range(1, dist + 1):
            ny = y + dy * i
            nx = x + dx * i
            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] == -1:
                    break
                elif graph[ny][nx] == 2:
                    graph[ny][nx] -= 1
                elif graph[ny][nx] == 1:
                    graph[ny][nx] = 0
                    queue.append((ny, nx, False))
                    broken += 1
                    not_broken -= 1

print(broken, not_broken)