def solution(s):
    answer = 0
    
    for x in range(len(s)):
        r = 0
        while x - r >= 0 and x + r < len(s) and s[x - r] == s[x + r]:
            r += 1
        answer = max(answer, r * 2 - 1)
        
        r = 0
        if x + 1 < len(s) and s[x] == s[x + 1]:
            while x - r >= 0 and x + 1 + r < len(s) and s[x - r] == s[x + 1 + r]:
                r += 1
        answer = max(answer, r * 2)
        
    return answer