from heapq import heappush, heappop
from collections import deque

def solution(priorities, location):
    answer = 0
    
    heap_queue = []
    order_queue = deque()
    
    for i in range(len(priorities)):
        p = priorities[i]
        heappush(heap_queue, -p)
        order_queue.append((-p, i))
    
    while order_queue:
        priority, idx = order_queue.popleft()
        
        if priority != heap_queue[0]:
            order_queue.append((priority, idx))
            continue
        
        heappop(heap_queue)
        answer += 1
        
        if idx == location:
            return answer
        
        
    
    return answer