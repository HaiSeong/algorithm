from collections import deque
from math import comb

n = int(input())
lst = list(map(int, input().split()))

dp = [0] * n
dp[0] = lst[0]
for i in range(1, n):
    dp[i] = lst[i] + dp[i - 1]

def get_sum(start, end):
    if start == end:
        return lst[start]
    return dp[end] - dp[start - 1]

print(get_sum(1, 1))
print(get_sum(1, 2))

answer = 0
for i in range(500000):
    answer += comb(500000 - i, 2) + comb(i, 2)
print(answer)