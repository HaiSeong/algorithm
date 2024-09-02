import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [{} for _ in range(n + 1)]

for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a][b] = w
    graph[b][a] = w
start, end = map(int, input().split())

answer = 0

queue = deque([(start, 1000000000)])
visited = {(start, 1000000000)}
while queue:
    now, weight = queue.popleft()

    if now == end:
        answer = max(answer, weight)
        continue

    for next in graph[now]:
        weight_next = graph[now][next]
        weight_next = min(weight, weight_next)
        if weight_next > answer and next != start:
            if (next, weight_next) not in visited:
                queue.append((next, weight_next))
                visited.add((next, weight_next))

print(answer)
