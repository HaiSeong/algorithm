
lines = [input() for _ in range(4)]
shotgun = input()

chars = dict()
count = [[0] * 10 for _ in range(4)]
for y in range(4):
    for x in range(10):
        chars[lines[y][x]] = (y, x)

for c in shotgun:
    y, x = chars[c]

    for i in range(-1, 2):
        for j in range(-1, 2):
            try:
                count[y + i][x+j] += 1
            except:
                pass

for i in range(4):
    for j in range(10):
        if count[i][j] == 9:
            print(lines[i][j])





