from collections import defaultdict

def solution(participant, completion):
    
    dic = {}
    all = 0
    
    for p in participant:
        dic[hash(p)] = p
        all += hash(p)
    for c in completion:
        all -= hash(c)
            
    return dic[all]