n = int(input())
lst = set(map(int, input().split()))
m = int(input())
lst2 = list(map(int, input().split()))

answer = []

for num in lst2:
    if num in lst:
        answer.append(1)
    else:
        answer.append(0)

print(*answer)