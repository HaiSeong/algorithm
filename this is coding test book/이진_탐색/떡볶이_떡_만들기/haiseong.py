
n, m = map(int, input().split())
lst = list(map(int, input().split()))

answer = 0
s = 0
e = max(lst)
while s < e:
    mid = (s + e) // 2

    cut = 0
    for l in lst:
        if l > mid:
            cut += l - mid

    if cut < m:
        e = mid - 1
    else:
        answer = mid
        s = mid + 1

print(answer)