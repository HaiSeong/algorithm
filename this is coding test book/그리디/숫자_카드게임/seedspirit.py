row, col = map(int, input().split())
answer = 0
for _ in range(row):
  candidate = sorted(list(map(int, input().split())))[0]
  if answer < candidate:
    answer = candidate

print(answer)