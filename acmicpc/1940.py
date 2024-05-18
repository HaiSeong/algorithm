
n = int(input())
m = int(input())
lst = list(map(int, input().split()))

answer = 0
lst.sort()
small, big = 0, n - 1

while small < big:
    num = lst[small] + lst[big]
    if num == m:
        answer += 1
        small += 1
        big -= 1
    elif num < m:
        small += 1
    else:
        big -= 1

print(answer)