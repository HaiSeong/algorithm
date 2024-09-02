
n, k = map(int, input().split())
inputs = [tuple(map(int, input().split())) for _ in range(k)]
inputs.sort()
x = []
t = []
s = []
for xx, tt, ss in inputs:
    x.append(xx)
    t.append(tt)
    s.append(ss)

time = 0
if k == 0:
    print(n)
    exit(0)

for i in range(k):
    if i == 0:
        time += x[i]
    else:
        time += x[i] - x[i - 1]

    # answer = s ~ s + t => 초록불
    # answer = s + t ~ s + 2t => 빨간불
    # t로 나눠서 몫이 홀수면 빨간불 => 2t 까지 기다려야함

    # if 0 <= answer - s[i] < t[i]:
    #     pass # 초록
    # if t[i] <= answer - s[i] < 2 * t[i]:
    #     pass # 빨간
    if time < s[i]:
        time = s[i]
    elif ((time - s[i]) // t[i]) % 2 != 0:
        time = ((time - s[i]) // t[i]) * t[i] + t[i] + s[i] # 빨간불 까지 대기

time += n - x[-1]
print(time)


