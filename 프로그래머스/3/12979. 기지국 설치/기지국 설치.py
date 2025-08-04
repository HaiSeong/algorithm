def solution(n, stations, w):
    answer = 0
    
    needs = []
    
    for i in range(len(stations) - 1):
        s1 = stations[i]
        s2 = stations[i + 1]
        
        needs.append(s2 - s1 - 2*w - 1)
    
    if stations[0] - w > 1:
        needs.append(stations[0] - w - 1)

    if stations[-1] + w < n:
        needs.append(n - stations[-1] - w)
        
    print(needs)
    
    for now in needs:
        answer += (now + 2 * w) // (2 * w + 1)
        
    return answer