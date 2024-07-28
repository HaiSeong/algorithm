n, l = map(int, input().split())

waters = [tuple(map(int, input().split())) for _ in range(n)]

waters.sort()

cnt = 0
now = 0
for start, end in waters:
    now = max(now, start)

    cnt += (end - now + l - 1) // l
    now += l * ((end - now + l - 1) // l)

print(cnt)


