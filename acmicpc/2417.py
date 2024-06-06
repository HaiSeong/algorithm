from math import sqrt

n = int(input())

cur = 0
step = n
while step > 0:
    while cur + step <= n and (cur + step) ** 2 < n:
        cur += step
    step //= 2

if n == 0:
    print(0)
else:
    print(cur + 1)
