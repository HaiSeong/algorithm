n = int(input())
lst = [(input().split()) for _ in range(n)]
lst.sort(key = lambda x:int(x[1]))

answer = []
for l in lst:
    answer.append(l[0])
print(*answer)