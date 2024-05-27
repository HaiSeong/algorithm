from collections import Counter

line = input()
visited = [False] * len(line)
quack = {
    'q': 0,
    'u': 1,
    'a': 2,
    'c': 3,
    'k': 4
}

def dfs(now, q):
    # print(now, line[now])
    visited[now] = True

    for next in range(now + 1, len(line)):
        if quack[line[next]] == (q + 1) % 5 and not visited[next]:
            dfs(next, (q + 1) % 5)
            break
    else:
        if q != 4:
            print(-1)
            exit(0)


c = Counter(line)
if len(c.keys()) != 5 or len(set(c.values())) != 1:
    print(-1)
    exit(0)

answer = 0
for i in range(len(line)):
    if not visited[i] and line[i] == 'q':
        # print('-' * 20)
        dfs(i, 0)
        answer += 1

print(answer)