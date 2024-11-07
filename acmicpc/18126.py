from heapq import heappop, heappush

n = int(input())
graph = [{} for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c

distances = [float('inf')] * (n + 1)
distances[1] = 0

queue = [1]

while queue:
    now = heappop(queue)
    dist = distances[now]

    for next in graph[now]:
        if distances[next] > dist + graph[now][next]:
            distances[next] = dist + graph[now][next]
            heappush(queue, next)

answer = max([d for d in distances if d != float('inf')])
print(answer)
