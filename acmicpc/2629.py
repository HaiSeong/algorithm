n = int(input())
weights = list(map(int, input().split()))
m = int(input())
lst = list(map(int, input().split()))

weights_dict = {weights[0]}
tmp = set()
for weight in weights[1:]:
    tmp.add(weight)
    for w in weights_dict:
        if weight - w >= 0:
            tmp.add(weight - w)
        else:
            tmp.add(w - weight)
        tmp.add(weight + w)
    for t in tmp:
        weights_dict.add(t)
    tmp.clear()

answer = []
for l in lst:
    if l in weights_dict:
        answer.append('Y')
    else:
        answer.append('N')

print(*answer)


