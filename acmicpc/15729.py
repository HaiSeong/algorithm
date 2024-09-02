n = int(input())
lst = list(map(int, input().split()))
now = [0] * n

cnt = 0

for i in range(n):
    if lst[i] == now[i]:
        continue

    now[i] = (now[i] + 1) % 2

    if i + 1 < n:
        now[i + 1] = (now[i + 1] + 1) % 2
    if i + 2 < n:
        now[i + 2] = (now[i + 2] + 1) % 2

    cnt += 1

print(cnt)