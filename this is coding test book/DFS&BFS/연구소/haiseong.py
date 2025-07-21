
from collections import deque, Counter
from itertools import combinations

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

spaces = []
viruses = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            spaces.append((i, j))
        if graph[i][j] == 2:
            viruses.append((i, j))

cases = list(combinations(spaces, 3))


def count(graph, visited):
    for wy, wx in case:
        graph[wy][wx] = 1
    for virus in viruses:
        dfs(graph, visited, virus)

    counter = Counter()
    for line in graph:
        counter += Counter(line)

    return counter[0]


def dfs(graph, visited, virus):
    queue = deque([virus])
    visited[virus[0]][virus[1]] = True

    while queue:
        y, x = queue.popleft()

        graph[y][x] = 2

        for dy, dx in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] == 0 and not visited[ny][nx]:
                    queue.append((ny, nx))
                    visited[ny][nx] = True


answer = 0
for case in cases:
    graph_cpy = [g[:] for g in graph]
    visited_cpy = [v[:] for v in visited]
    cnt = count(graph_cpy, visited_cpy)
    answer = max(answer, cnt)

print(answer)
