r, c = map(int, input().split())
n = int(input())
lst = list(map(int, input().split()))

lst.sort(reverse=True)

answer = 0
i = 0
while i < n:
    j = 0
    while i + j < n and j < c and lst[i + j] == lst[i]:
        j += 1
        answer += 1
    while i + j < n  and lst[i + j] == lst[i]:
        j += 1
    i += j

answer = min(r * c, answer)
print(answer)
