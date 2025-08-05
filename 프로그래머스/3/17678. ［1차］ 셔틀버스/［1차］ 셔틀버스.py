def tt(t_str):
    return int(t_str[:2]) * 60 + int(t_str[3:])

def solution(n, t, m, timetable):
    people = [tt(t_) for t_ in timetable]
    people.sort()
    # print(people)
    
    buses = {9*60 + t * i : [] for i in range(n)}
    # print(buses)
    
    p = 0
    for bus in buses:
        while p < len(people) and len(buses[bus]) < m:
            if bus >= people[p]:
                buses[bus].append(people[p])
                p+=1
            else:
                break
    
    # print(buses)
    
    lastBusTime = max(buses)
    lastBus = buses[lastBusTime]
    answer = 0
    # print("last", lastBus)
    if len(lastBus) >= m:
        answer = max(lastBus) - 1
    else:
        answer = lastBusTime
                
    
    return "%02d:%02d"%(answer // 60, answer % 60)