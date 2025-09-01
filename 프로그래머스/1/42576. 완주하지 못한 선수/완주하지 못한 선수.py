from collections import defaultdict

def solution(participant, completion):
    participant_dict = defaultdict(int)
    completion_dict = defaultdict(int)
    
    for p in participant:
        participant_dict[p] += 1
        
    for c in completion:
        completion_dict[c] += 1
        
    answer = ""
    for p in participant:
        if participant_dict[p] != completion_dict[p]:
            answer = p
            break
    
    return answer