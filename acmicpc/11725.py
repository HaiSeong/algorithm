from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
parents = [0] * (n+1)

for _ in range(n-1):
    v, u = map(int, input().split())
    graph[v].append(u)
    graph[u].append(v)

queue = deque([(1, 0)])
visited = set()

while queue:
    now, p = queue.popleft()
    parents[now] = p

    for next in graph[now]:
        if next not in visited:
            queue.append((next, now))
            visited.add(next)

for p in parents[2:]:
    print(p)