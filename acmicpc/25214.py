
n = int(input())
lst = list(map(int, input().split()))

min_num = lst[0]
now = 0
answer = [0]

for a in lst[1:]:
    min_num = min(min_num, a)

    if now <= a - min_num:
        now = a - min_num

    answer.append(now)

print(*answer)

