
n, m = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))

apps = [(a[i], c[i]) for i in range(n)]

apps.sort(key=lambda app: (app[1], -app[0]))

# print(apps)

memory = {0: 0}
answer = float('inf')

for app in apps:
    mem, co = app
    for before in set(memory.keys()):
        if before + mem not in memory:
            memory[before + mem] = float('inf')

        if answer > memory[before] + co:
            memory[before + mem] = min(memory[before + mem], memory[before] + co)
            answer = min([float('inf')] + [memory[me] for me in memory if me >= m])

print(answer)