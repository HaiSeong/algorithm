
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

def bfs(sy, sx):
    queue = deque([(sy, sx)])
    visited[sy][sx] = True

    while queue:
        y, x = queue.popleft()

        for dy, dx in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] == 0 and not visited[ny][nx]:
                    queue.append((ny, nx))
                    visited[ny][nx] = True


answer = 0
for sy in range(n):
    for sx in range(m):
        if graph[sy][sx] == 0 and not visited[sy][sx]:
            bfs(sy, sx)
            answer += 1

print(answer)
