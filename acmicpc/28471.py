from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
graph = [input().strip() for _ in range(n)]

start = (0, 0)
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'F':
            start = (i, j)
            break

queue = deque([start])
visited = [[False] * n for _ in range(n)]
visited[start[0]][start[1]] = True

answer = 0
while queue:
    y, x = queue.popleft()

    if not (y == start[0] and x == start[1]):
        answer += 1

    for dy, dx in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 1)]:
        ny = dy + y
        nx = dx + x
        if 0 <= ny < n and 0 <= nx < n:
            if graph[ny][nx] != '#' and not visited[ny][nx]:
                queue.append((ny, nx))
                visited[ny][nx] = True

print(answer)


