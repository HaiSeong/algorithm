from collections import deque


# 1001
# 1010
# 0011

n = int(input())

def nat(num):
    return ((1 << n) - 1) - num

def xor(num, mask):
    return (num & nat(mask)) | (nat(num) & mask)

statuses = list(map(int, input().split()))

maskes = []
for i in range(n):
    line = list(map(int, input().split()))
    mask = 1 << (n - i - 1)
    for b in line[1:]:
        mask += (1 << (n - b ))
    maskes.append(mask)
# print(maskes)
start = 0
for s in statuses:
    start <<= 1
    start |= s

end = nat(0)
visited = {start}
queue = deque([(start, 0)])
answer = -1
# print(start)
# print(end)
while queue:
    now, time = queue.popleft()

    # print(now)
    if now == end:
        answer = time
        break

    for i, mask in enumerate(maskes):
        if (now >> (n - i - 1)) & 1 == 0:
            next = xor(now, mask)
            # print(now, i, mask, next)
            if next not in visited:
                queue.append((next, time + 1))
                visited.add(next)


print(answer)