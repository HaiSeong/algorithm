from collections import deque

n = int(input())
lst = list(map(int, input().split()))
k = int(input())

start = 1
queue = deque([(start, 1)])
distance = {1:1}

while queue:
    now, count = queue.popleft()

    if count > k:
        break

    for add in lst:
        next = now + add
        if next not in distance:
            distance[next] = count + 1
            queue.append((next, count + 1))

answer = 1
while answer in distance:
    answer += 1

if answer %2 == 0:
    print("jjaksoon win at " + str(answer - 1))
else:
    print("holsoon win at " + str(answer - 1))


