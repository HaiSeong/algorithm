def solution(s):
    answer = len(s)
    for length in range(1, len(s) // 2 + 1):
        lst = [s[i * length: (i + 1) * length] for i in range(0, len(s) // length + 1)]
        if len(lst[-1]) == 0:
            lst.pop()
        ans = 0
        i = 0
        while i < len(lst):
            j = i + 1
            cnt = 1
            while j < len(lst) and lst[i] == lst[j]:
                cnt += 1
                j += 1
            ans += len(lst[i])
            if cnt > 1:
                ans += len(str(cnt))
            i = j
        answer = min(answer, ans)

    return answer

print("aabbaccc:", solution("aabbaccc"))
print("ababcdcdababcdcd:", solution("ababcdcdababcdcd"))
print("abcabcdede:", solution("abcabcdede"))
print("abcabcabcabcdededededede:", solution("abcabcabcabcdededededede"))
print("xababcdcdababcdcd:", solution("xababcdcdababcdcd"))