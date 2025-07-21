import bisect

n, x = map(int, input().split())
lst = list(map(int, input().split()))

left = bisect.bisect_left(lst, x)
right = bisect.bisect_right(lst, x)

if right == left:
    print(-1)
else:
    print(right - left)