position = input()

ps = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8}
dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

answer = 0
for i in range(len(dx)):
  x = ps[position[0]] + dx[i]
  y = int(position[1])+ dy[i]

  if (x > 8) or (x < 1) or (y > 8) or (y < 1):
    continue
  answer += 1

print(answer)