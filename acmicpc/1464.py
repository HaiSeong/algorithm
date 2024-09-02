from collections import deque

line = input()

queue = deque([line[0]])
for c in line[1:]:
    if queue[0] < c:
        queue.append(c)
    else:
        queue.appendleft(c)
print(''.join(list(queue)))
