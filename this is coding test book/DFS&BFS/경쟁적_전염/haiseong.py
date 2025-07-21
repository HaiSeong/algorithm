from collections import deque

n, k, = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
s, Y, X = map(int, input().split())

visited = [[False] * n for _ in range(n)]

virus = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            virus.append((i, j, graph[i][j], 0))
            visited[i][j] = True

queue = deque(sorted(virus, key=lambda x: x[2]))

while queue:
    y, x, num, t = queue.popleft()

    if t > s:
        break
    graph[y][x] = num

    for dy, dx in [(0, -1,), (0, 1), (-1, 0), (1, 0)]:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < n and 0 <= nx < n:
            if graph[ny][nx] == 0 and not visited[ny][nx]:
                queue.append((ny, nx, num, t + 1))
                visited[ny][nx] = True

print(graph[Y - 1][X - 1])
