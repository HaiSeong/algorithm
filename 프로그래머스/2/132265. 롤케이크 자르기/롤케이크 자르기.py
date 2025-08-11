def solution(topping):
    
    right = {}
    left = {}
    n = len(topping)
    for t in topping:
        if t not in left:
            left[t] = 0
        left[t] += 1
    
    cntRight = 0
    cntLeft = len(left)
    answer = 0
    for i in range(n):
        t = topping[i]
        if t not in right:
            right[t] = 0
            cntRight += 1
        right[t] += 1
        
        left[t] -= 1
        if left[t] == 0:
            cntLeft -= 1
        
        if cntRight == cntLeft:
            answer += 1
        
    return answer
        