COUNT = 0
TIME = 1

n, m = map(int ,input().split())
lives = [tuple(input().split()) for _ in range(n)]

lives.sort()

bjs = {}

for live in lives:
    name, day = live[0], int(live[1]) - 1
    hour1, sec1 = map(int, live[2].split((":")))
    hour2, sec2 = map(int, live[3].split((":")))
    time = 60 * hour2 + sec2 - 60 * hour1 - sec1

    if name not in bjs:
        bjs[name] = [[0, 0] for _ in range(m // 7)] # (count, time) for weeks

    bjs[name][day // 7][COUNT] += 1
    bjs[name][day // 7][TIME] += time


answer = []
for name in bjs:
    real = True
    count_time_list = bjs[name]
    for count_time in count_time_list:
        count, time = count_time[0], count_time[1]
        if count < 5 or time < 60 * 60:
            real = False
            break
    if real:
        answer.append(name)

answer.sort()
if len(answer) == 0:
    print(-1)
else:
    print("\n".join(answer))
