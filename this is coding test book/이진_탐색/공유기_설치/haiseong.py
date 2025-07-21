import sys
input = sys.stdin.readline

n, c = map(int,input().split())
homes = [int(input()) for _ in range(n)]
homes.sort()

max_gap = homes[-1] - homes[0]
min_gap = 1
result = 0

while min_gap <= max_gap:
    gap = (min_gap + max_gap) // 2
    now = homes[0]

    cnt = 1
    for i in range(1,n):
        if homes[i] >= now + gap:
            now = homes[i]
            cnt+=1

    if cnt >= c:
        min_gap = gap+1
        result = gap
    else:
        max_gap = gap-1

print(result)