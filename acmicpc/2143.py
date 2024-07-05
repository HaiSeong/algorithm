from collections import defaultdict

t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

dp_a = a[:]
for i in range(1, n):
    dp_a[i] += dp_a[i-1]
dp_b = b[:]
for i in range(1, m):
    dp_b[i] += dp_b[i-1]

sums_a = defaultdict(int)
sums_b = defaultdict(int)
for i in range(n):
    for j in range(i + 1, n):
        sums_a[dp_a[j] - dp_a[i]] += 1
    sums_a[dp_a[i]] += 1
for i in range(m):
    for j in range(i + 1, m):
        sums_b[dp_b[j] - dp_b[i]] += 1
    sums_b[dp_b[i]] += 1

answer = 0
for num in sums_a:
    answer += sums_b[t - num] * sums_a[num]
print(answer)
