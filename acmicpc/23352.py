from collections import deque

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

answer_length = 0
answer = 0


def bfs(sy, sx):
    global answer, answer_length

    visited = [[False] * m for _ in range(n)]

    queue = deque([(sy, sx, 0)])
    visited[sy][sx] = True

    while queue:
        y, x, dist, = queue.popleft()

        if answer_length < dist:
            answer_length = dist
            answer = graph[sy][sx] + graph[y][x]
        if answer_length == dist:
            answer_length = dist
            answer = max(answer, graph[sy][sx] + graph[y][x])

        for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ny, nx = y + dy, x + dx

            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] != 0 and not visited[ny][nx]:
                    queue.append((ny, nx, dist + 1))
                    visited[ny][nx] = True

for i in range(n):
    for j in range(m):
        if graph[i][j] != 0:
            bfs(i, j)

print(answer)