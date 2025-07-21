s = map(int, input())
answer = 0

for number in s:
    if number <= 1 or answer == 0:
        answer += number
    else:
        answer *= number
    
print(answer)