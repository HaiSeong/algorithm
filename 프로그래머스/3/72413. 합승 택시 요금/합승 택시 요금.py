from heapq import heappush, heappop

def get_cost(graph, n, start, end):
    
    costs = [float('inf')] * (n + 1)
    costs[start] = 0
    
    queue = [(0, start)]
    
    while queue:
        dist, now = heappop(queue)
        
        if now == end:
            return dist
        
        for next in graph[now]:
            if costs[next] > dist + graph[now][next]:
                costs[next] = dist + graph[now][next]
                heappush(queue, (costs[next], next))
            
    return costs[end]

def solution(n, s, a, b, fares):
    answer = 0
    
    graph = {p : dict() for p in range(1, n + 1)}
    
    for p1, p2, cost in fares:
        graph[p1][p2] = cost
        graph[p2][p1] = cost
    
    answer = float('inf')
    for c in range(1, n + 1):
        c1 = get_cost(graph, n, s, c)
        c2 = get_cost(graph, n, c, a)
        c3 = get_cost(graph, n, c, b)
    
        answer = min(answer, sum([c1, c2, c3]))
    
    return answer