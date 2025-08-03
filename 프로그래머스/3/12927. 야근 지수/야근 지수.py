from heapq import heapify, heappop, heappush

def solution(n, works):
    
    works = list(map(lambda x: -x, works))    
    heapify(works)
    
    while n > 0:
        n -= 1
        w = heappop(works)
        if w == 0:
            break
        heappush(works, w + 1)
        
    
    answer = 0
    for w in works:
        answer += w*w
    return answer