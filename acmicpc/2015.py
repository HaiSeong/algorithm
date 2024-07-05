
n, k = map(int, input().split())
lst = list(map(int, input().split()))
sums = [0] * (n)

for i in range(n):
    sums[i] = sums[i - 1] + lst[i]

answer = 0

sums_dict = {}
for s in sums:
    if s - k in sums_dict:
        answer += sums_dict[s - k]
    if s == k:
        answer+=1

    if s not in sums_dict:
        sums_dict[s] = 0
    sums_dict[s] += 1
    print(sums_dict)
print(answer)