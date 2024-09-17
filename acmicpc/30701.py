from collections import deque

n, d = map(int, input().split())

monsters = []
weapons = []
for _ in range(n):
    info, x = map(int, input().split())
    if info == 1:
        monsters.append(x)
    else:
        weapons.append(x)
monsters = sorted(monsters)
weapons = deque(sorted(weapons))

answer = 0
dead = False
for monster in monsters:
    while d <= monster:
        if not weapons:
            dead = True
            break
        d *= weapons.popleft()
        answer += 1

    if dead:
        break

    d += monster
    answer += 1

if not dead:
    answer = n

print(answer)