s = input()
result = []
cnt = 1

for i in range(1, len(s)//2+2):
    answer = ''
    same_check_list = s[:i]
    
    for j in range(i, len(s)+i, i):
        if same_check_list == s[j:j+i]: # 만약 현재가 전과 같다면
            cnt += 1
        else:
            if cnt == 1:
                answer += same_check_list
            else:
                answer += str(cnt) + same_check_list
            same_check_list = s[j:j+i]
            cnt = 1
    result.append(len(answer))

print(min(result)) 