n = int(input())
limits = list(map(int,input().split()))
m = int(input())
boxes = list(map(int,input().split()))

limits.sort()
boxes.sort(reverse=True)
counts = [0] * n

if max(limits) < max(boxes):
    print(-1)
    exit(0)

for box in boxes:
    for i in range(n):
        if limits[i] >= box:
            counts[i] += 1
            break

# print(limits)
# print(counts)
# [23, 25, 28, 32]
# [7, 1, 1, 1]

for i in range(n - 1):
    # print(sum(counts[i:]) / (n-i))
    # print(counts[i])
    # print()
    while counts[i] > sum(counts[i:]) / (n-i):
        counts[i + 1] += 1
        counts[i] -= 1

print(max(counts))
