from collections import deque

n, m = map(int, input().split())

graph = [input() for _ in range(n)]
visited = [[False] * m for _ in range(n)]
answer_sheep = 0
answer_wolf = 0

def bfs(sy, sx):
    global answer_sheep, answer_wolf
    queue = deque([(sy, sx)])
    visited[sy][sx] = True
    sheep = 0
    wolf = 0

    while queue:
        y, x = queue.popleft()

        if graph[y][x] == 'o':
            sheep += 1
        if graph[y][x] == 'v':
            wolf += 1

        for dy, dx in [(0,1),(1,0),(0,-1),(-1,0)]:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < n and  0 <= nx < m:
                if graph[ny][nx] != '#' and not visited[ny][nx]:
                    queue.append((ny,nx))
                    visited[ny][nx] = True

    if sheep > wolf:
        answer_sheep += sheep
    else:
        answer_wolf += wolf

for sy in range(n):
    for sx in range(m):
        if graph[sy][sx] != '#' and  not visited[sy][sx]:
            bfs(sy, sx)

print(answer_sheep, answer_wolf)
