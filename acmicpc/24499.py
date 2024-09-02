from collections import deque

n, k = map(int, input().split())
lst = list(map(int, input().split()))

sums = sum(lst[:k])
answer = sums
for i in range(k, n + k):
    sums += lst[(i) % n]
    sums -= lst[(i - k) % n]
    answer = max(sums, answer)

print(answer)


