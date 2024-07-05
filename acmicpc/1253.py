from collections import defaultdict

n = int(input())
lst = list(map(int, input().split()))

lst.sort()
num_cnts = defaultdict(int)
for num in lst:
    num_cnts[num] += 1
sums = set()

for i in range(n):
    for j in range(i + 1, n):
        zc = 0
        if lst[i] == 0:
            zc += 1
        if lst[j] == 0:
            zc += 1
        if zc == 2 and num_cnts[0] < 3:
            continue
        if zc == 1 and num_cnts[lst[i] + lst[j]] <= 1:
            continue

        sums.add(lst[i] + lst[j])

answer = 0
for num in lst:
    if num in sums:
        answer += 1

if n < 3:
    answer = 0

print(answer)
