import heapq

N = int(input())

heap = [int(input()) for _ in range(N)]
heapq.heapify(heap)

answer=0

while len(heap) > 1:
    first = heapq.heappop(heap)
    second = heapq.heappop(heap)
    answer += first + second
    heapq.heappush(heap, first + second)

print(answer)