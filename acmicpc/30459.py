n, m, r = map(int, input().split())
mals = list(map(int, input().split()))
gits = list(map(int, input().split()))
gits.sort()
answer = -1
for i in range(n):
    for j in range(i + 1, n):
        bottom = abs(mals[i] - mals[j])

        cur = -1
        step = m
        while step > 0:
            while cur + step < m and bottom * gits[cur + step] <= r * 2:
                cur += step
            step //= 2

        if cur > -1:
            answer = max(answer, bottom * gits[cur] / 2)

if answer == -1:
    print(-1)
else:
    print("%.1lf"%answer)