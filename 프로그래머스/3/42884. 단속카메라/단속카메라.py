def solution(routes):
    answer = 1
    
    routes.sort(key = lambda x : (x[0], -x[1]))
    print(routes)
    start, end = -30000, 30000
    for s, e in routes:
        if end < start:
            print(s, e)
            answer += 1
            start = s
            end = e
            continue
        
        if max(s, start) > min(e, end):
            answer += 1
            start = s
            end = e
            continue
        
        
        start = max(s, start)
        end = min(e, end)
        
        print(start, end)
            
    
    return answer