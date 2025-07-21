import heapq

answer = []
h = []
heapq.heappush(h, 1)

n = int(input())
while len(answer) < n:
    pop = heapq.heappop(h)
    answer.append(pop)
    for i in [2, 3, 5]:
        if pop * i not in h:
            heapq.heappush(h, pop * i)

print(answer[-1])