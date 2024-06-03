from collections import deque
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]


    def bfs(sy, sx):
        queue = deque([(sy, sx)])
        visited[sy][sx] = True

        while queue:
            y, x = queue.popleft()

            for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ny = dy + y
                nx = dx + x
                if 0 <= ny < n and 0 <= nx < m:
                    if not visited[ny][nx] and graph[ny][nx] == 1:
                        queue.append((ny,nx))
                        visited[ny][nx] = True

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    answer = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                answer += 1

    print(answer)