import heapq
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
p = int(input())
ps = set(list(map(int, input().split())))

answer = float('inf')

queue = ([(0, start, False)])
distance = [float('inf')] * (n + 1)

while queue:
    dist, now, visit_p = heapq.heappop(queue)

    if end == now and visit_p:
        answer = min(dist, answer)

    if not visit_p and now in ps:
        visit_p = True

    if dist > answer:
        break

    for next in graph[now]:
        if next == end and not visit_p:
            continue
        if dist + graph[now][next] < distance[next]:
            distance[next] = dist + graph[now][next]
            heapq.heappush(queue, (distance[next], next, visit_p))

if answer == float('inf'):
    answer = -1
print(answer)
