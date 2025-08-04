def solution(routes):
    answer = 0
    
    routes.sort(key = lambda x : x[1])
    last = -30001
    
    print(routes)
    
    for s, e in routes:
        if s > last:
            answer += 1
            last = e
            
    return answer