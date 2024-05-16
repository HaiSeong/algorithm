from collections import deque

n = int(input())
lst = list(map(int, input().split()))

queue = deque()
start = 0
answer = 0
last_index = {i : 0 for i in range(1, 10)}

for i, a in enumerate(lst):
    last_index[a] = i
    if a in queue:
        pass
    elif len(queue) < 2:
        queue.append(a)
    else:
        queue.append(a)
        pop = queue.popleft()
        start = last_index[pop] + 1
    answer = max(answer, i - start + 1)


print(answer)