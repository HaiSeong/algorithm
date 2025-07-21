from collections import deque

n, m, k, x = map(int, input().split())

graph = {node: set() for node in range(1, n + 1)}

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].add(e)

visited = {node: False for node in range(1, n + 1)}

answer = []
queue = deque([(x, 0)])
visited[x] = True

while queue:
    now, dist = queue.popleft()

    if dist > k:
        break
    if dist == k:
        answer.append(now)

    for next in graph[now]:
        if not visited[next]:
            queue.append((next, dist + 1))
            visited[next] = True

if len(answer) == 0:
    print(-1)
else:
    answer.sort()
    for ans in answer:
        print(ans)
