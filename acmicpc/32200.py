from collections import deque

n, x, y = map(int, input().split())
sandwiches = deque(list(map(int, input().split())))

answer_day = 0
answer_left = 0

for sandwich in sandwiches:
    day = sandwich // x
    left = sandwich % x - day * (y - x)
    left = max(left, 0)

    answer_day += day
    answer_left += left

print(answer_day)
print(answer_left)
