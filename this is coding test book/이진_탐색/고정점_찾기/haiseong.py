
n =  int(input())
lst = list(map(int, input().split()))

s = 0
e = n-1

answer = -1
while s <= e:
    m = (s + e) // 2

    if lst[m] == m:
        answer = m
        break
    elif lst[m] < m:
        s = m + 1
    else:
        e = m - 1

print(answer)