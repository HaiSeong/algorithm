
n = int(input())
lst = list(map(int, input().split()))
m = int(input())


def check(num):
    return sum(min(l, num) for l in lst) <= m


cur = -1
end = max(lst)
step = end + 1
while step > 0:
    while cur + step <= end and check(cur + step):
        cur += step
    step //= 2

print(cur)