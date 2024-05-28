from collections import Counter

n, m, b = map(int, input().split())

counts = Counter()
for _ in range(n):
    counts = counts + Counter(map(int, input().split()))

counts_keys = list(sorted(counts.keys(), reverse=True))
answer = (float('inf'), float('inf'))
for height in range(256, -1, -1):
    inventory = b
    cost = 0
    for h in counts_keys:
        if h > height:
            cost += 2 * (h - height) * counts[h]
            inventory += (h - height) * counts[h]
        elif h < height:
            cost += (height - h) * counts[h]
            inventory -= (height - h) * counts[h]
    if inventory >= 0 and cost < answer[0]:
        answer = (cost, height)

print(*answer)
