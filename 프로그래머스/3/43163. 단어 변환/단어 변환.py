from collections import deque

def solution(begin, target, words):
    
    if target not in words:
        return 0
    words.append(begin)
    
    graph = {w:set() for w in words}
    visited = {w:False for w in words}
    
    for w1 in words:
        for w2 in words:
            if w1 == w2:
                continue
                
            cnt = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    cnt += 1
                    if cnt >= 2:
                        break
            if cnt == 1:
                graph[w1].add(w2)
                graph[w2].add(w1)
                
    visited[begin] = True
    queue = deque([(begin, 0)])
    
    while queue:
        now, dist = queue.popleft()
        
        if now == target:
            return dist
        
        for next in graph[now]:
            if not visited[next]:
                queue.append((next, dist + 1))
    
    return 0