from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(n)]
visited = [[False] * m for _ in range(n)]


def dfs(sy, sx):
    queue = deque([(sy, sx, 1)])
    visited[sy][sx] = True

    while queue:
        y, x, dist = queue.popleft()

        if y == n - 1 and x == m - 1:
            return dist

        for dy, dx in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] == 1 and not visited[ny][nx]:
                    queue.append((ny, nx, dist + 1))
                    visited[ny][nx] = True


print(dfs(0, 0))
