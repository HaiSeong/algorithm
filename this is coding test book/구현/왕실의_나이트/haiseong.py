pos = input()
sx = ord(pos[0]) - ord('a')
sy = int(pos[1]) - 1

answer = 0
for dy, dx in [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)]:
    ny = sy + dy
    nx = sx + dx
    if 0 <= ny < 8 and 0 <= nx < 8:
        answer += 1

print(answer)