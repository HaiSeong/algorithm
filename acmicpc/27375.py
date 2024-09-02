from collections import deque

n, k = map(int, input().split())
classes = [tuple(map(int, input().split())) for _ in range(n)]

classes.sort()


queue = deque([(0, 0, 0)])

for day, start, end in classes:

    if day >= 5:
        break

    tmp = []
    while queue:
        point, last_day, last_end = queue.popleft()

        if point > k:
            continue

        # 들을수도 있고
        if day > last_day or (day == last_day and start > last_end):
            tmp.append((point + end - start + 1, day, end))

        # 안들을 수도 있고
        tmp.append((point, last_day, last_end))

    for t in tmp:
        queue.append(t)


answer = 0
for point, last_day, last_end in queue:
    if point == k:
        answer+= 1

print(answer)