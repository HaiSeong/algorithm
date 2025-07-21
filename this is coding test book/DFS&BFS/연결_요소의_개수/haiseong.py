from collections import deque

n, m = map(int, input().split())
graph = {x: set() for x in range(1, n + 1)}

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

visited = [False] * (n + 1)

def bfs(start):
    visited[start] = True
    queue = deque([start])

    while queue:
        now = queue.popleft()

        for next in graph[now]:
            if not visited[next]:
                queue.append(next)
                visited[next] = True

answer = 0
for start in range(1, n+1):
    if not visited[start]:
        bfs(start)
        answer += 1
print(answer)