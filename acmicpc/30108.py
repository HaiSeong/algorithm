import heapq, sys

input = sys.stdin.readline

n = int(input())
parents = [0, 0] + list(map(int, input().split()))
lst = [0] + list(map(int, input().split()))

tree = {i: [] for i in range(n + 1)}
for i in range(1, n+1):
    tree[parents[i]].append(i)

heap = [(0, 0)]
answer = 0
answers = []

while heap:
    point_minus, now = heapq.heappop(heap)
    answer -= point_minus

    for next in tree[now]:
        heapq.heappush(heap, (-lst[next], next))

    answers.append(str(answer))

print('\n'.join(answers[1:]))