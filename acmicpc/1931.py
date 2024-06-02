n = int(input())
meetings = [list(map(int, input().split())) for _ in range(n)]

meetings.sort(key=lambda m: (m[1], m[0]))

cnt = 0
last = 0

for m in meetings:
    if m[0] >= last:
        cnt += 1
        last = m[1]

print(cnt)
