from itertools import combinations

must = set('antatica')
n, k = map(int, input().split())
words = [set(input()).difference(must) for _ in range(n)]

if k < 5:
    print(0)
    exit(0)

cases = list(combinations('qweryuopsdfghjklzxvbm', max(0, k - 5)))
answer = 0
for case in cases:
    learn = set(case)
    cnt = 0
    for word in words:
        for c in word:
            if c not in learn:
                break
        else:
            cnt += 1
    answer = max(answer, cnt)

print(answer)
