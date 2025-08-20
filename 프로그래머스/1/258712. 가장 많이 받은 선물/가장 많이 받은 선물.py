# 선물 지수 = 이번 달까지 자신이 친구들에게 준 선물의 수 - 받은 선물의 수

def solution(friends, gifts):
    answer = 0
    next_months = {f:0 for f in friends}
    
    gift_scores = {f:0 for f in friends}
    graph = {friend : {} for friend in friends}
    for friend in graph:
        for f in friends:
            graph[friend][f] = 0
            
    for g in gifts:
        a, b = g.split()

        graph[a][b] += 1
        graph[b][a] -= 1

        gift_scores[a] += 1
        gift_scores[b] -= 1
        
    for i in range(len(friends)):
        for j in range(i + 1, len(friends)):
            a = friends[i]
            b = friends[j]
            
            if graph[a][b] > 0:
                next_months[a] += 1
            elif graph[a][b] < 0:
                next_months[b] += 1
            elif gift_scores[a] > gift_scores[b]:
                next_months[a] += 1
            elif gift_scores[a] < gift_scores[b]:
                next_months[b] += 1
            
    answer = max(next_months.values())
    return answer