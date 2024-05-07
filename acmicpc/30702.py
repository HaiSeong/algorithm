from collections import deque

n, m = map(int, input().split())

a = [list(input()) for _ in range(n)]
b = [list(input()) for _ in range(n)]
answer = [['0'] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]


def bfs(sy, sx):
    queue = deque([(sy, sx)])
    visited[sy][sx] = True

    while queue:
        y, x, = queue.popleft()

        answer[y][x] = b[sy][sx]

        for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ny = dy + y
            nx = dx + x
            if 0 <= ny < n and 0 <= nx < m:
                if not visited[ny][nx]:
                    if a[ny][nx] == a[sy][sx]:
                        queue.append((ny, nx))
                        visited[ny][nx] = True


for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            bfs(i, j)

result = 'YES'
for i in range(n):
    for j in range(m):
        if b[i][j] != answer[i][j]:
            result = 'NO'

print(result)

