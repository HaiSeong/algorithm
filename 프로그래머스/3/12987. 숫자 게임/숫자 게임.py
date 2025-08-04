from collections import deque

def solution(A, B):
    
    A = deque(sorted(A))
    B = deque(sorted(B))

    answer = 0
    
    while A and B:
        a = A.popleft()
        b = -1
        while B and a >= b:
            b = B.popleft()
        
        if a < b:
            answer += 1
        
        
        
                
    return answer