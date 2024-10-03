def check(w, cur):
    global bag_sizes, occupieds

    if w > bag_sizes[cur]:
        return False
    if occupieds[cur]:
        return False

    return True

def get_bag_index(w):
    global goods, bag_sizes, occupieds

    cur = -1
    step = len(bag_sizes)
    while step > 0:
        while cur + step < len(bag_sizes) and check(w, cur + step):
            cur += step
        step //= 2

    if cur == -1:
        return -1

    # occupieds = occupieds[:cur] + occupieds[cur + 1:]
    # bag_sizes = bag_sizes[:cur] + bag_sizes[cur + 1:]
    occupieds[cur] = True
    return cur


n, k = map(int, input().split())
goods = [tuple(map(int, input().split())) for _ in range(n)] # w, c
bag_sizes = [int(input()) for _ in range(k)]
occupieds = [False] * k

goods.sort(key= lambda g : (-g[1], g[0]))
bag_sizes.sort()

answer = 0

for w, c in goods:
    index = get_bag_index(w)

    if index == -1:
        continue

    answer += c

print(answer)