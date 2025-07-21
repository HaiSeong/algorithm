# 첫번째 풀이
N, M = map(int, input().split())
row, col, d = map(int, input().split())

total_map = []
for _ in range(N):
  tmp = list(map(int, input().split()))
  total_map.append(tmp)


move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
answer = 0

while True:
  for i in range(len(move)):
    i = d
    if i > 3:
      i = i - 4
    tmp_row = row + move[i][0]
    tmp_col = col + move[i][1]
    if total_map[tmp_row][tmp_col] == 1:
      print(f"중간:{answer}")
      continue

    answer += 1
    total_map[row][col] = 1
    row = tmp_row
    col = tmp_col

print(answer)


# 두번째 풀이
N, M = map(int, input().split())
row, col, dir = map(int, input().split())

# 방문 기록을 위한 리스트 생성
memo = [[0] * M for _ in range(N)]
print(memo)

# 게임 맵 생성
total_map = []
for _ in range(N):
  total_map.append(list(map(int, input().split())))

def turn_left():
  global dir
  dir -= 1
  if dir == -1:
    dir = 3

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

answer = 1
turn_time = 0
memo[row][col] = 1

while True:

  turn_left()
  tmp_row = row + drow[dir]
  tmp_col = col + dcol[dir]

  if memo[tmp_row][tmp_col] == 0 and total_map[tmp_row][tmp_col] == 0:
    answer += 1
    turn_time = 0
    row = tmp_row
    col = tmp_col
    memo[row][col] = 1

  else:
    if turn_time == 4:
      row = row + abs(drow[dir])
      col = col + abs(dcol[dir])
      if total_map[row][col] == 1:
        break
    else:
      turn_time += 1

print(answer)