from collections import deque

n, m, v = map(int, input().split())
graph = {x: list() for x in range(1, n + 1)}

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph:
    graph[g].sort()

def dfs(start):
    answer = []

    visited = [False] * (n + 1)
    stack = deque([start])

    while stack:
        now = stack.pop()

        if not visited[now]:
            visited[now] = True

            answer.append(now)

            for next in graph[now][::-1]:
                stack.append(next)

    print(' '.join(map(str, answer)))

def bfs(start):
    answer = []

    visited = [False] * (n + 1)
    visited[start] = True
    queue = deque([start])

    while queue:
        now = queue.popleft()

        answer.append(now)

        for next in graph[now]:
            if not visited[next]:
                queue.append(next)
                visited[next] = True

    print(' '.join(map(str, answer)))

dfs(v)
bfs(v)
