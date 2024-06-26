import heapq

left = []
right = []

n = int(input())
lst = list(map(int, input().split()))

answer = 0

for start in range(n - 1):
    heapq.heappush(right, (lst[start], lst[start]))
    for end in range(start+1, n):
        heapq.heappush(right, (lst[end], lst[end]))

        while len(left) < len(right):
             pop = heapq.heappop(right)[1]
             heapq.heappush(left, (-pop, pop))

        answer = max(left[0][1], answer)

    left = []
    right = []

print(answer)

