# 1 i x : i번째 기차에(1 ≤ i ≤ N) x번째 좌석에(1 ≤ x ≤ 20) 사람을 태워라. 이미 사람이 타있다면 , 아무런 행동을 하지 않는다.
# 2 i x : i번째 기차에 x번째 좌석에 앉은 사람은 하차한다. 만약 아무도 그자리에 앉아있지 않았다면, 아무런 행동을 하지 않는다.
# 3 i : i번째 기차에 앉아있는 승객들이 모두 한칸씩 뒤로간다. k번째 앉은 사람은 k+1번째로 이동하여 앉는다. 만약 20번째 자리에 사람이 앉아있었다면 그 사람은 이 명령 후에 하차한다.
# 4 i : i번째 기차에 앉아있는 승객들이 모두 한칸씩 앞으로간다. k번째 앉은 사람은 k-1 번째 자리로 이동하여 앉는다. 만약 1번째 자리에 사람이 앉아있었다면 그 사람은 이 명령 후에 하차한다.

n, m = map(int, input().split())

trains = [0 for _ in range(n+1)]
for _ in range(m):
    line = input()

    if line[0] == '1':
        command, i, x = map(int, line.split())
        bits = 1 << (x - 1)
        trains[i] |= bits
    elif line[0] == '2':
        command, i, x = map(int, line.split())
        bits = (1 << 20) - 1
        bits -= 1 << (x - 1)
        trains[i] &= bits
    elif line[0] == '3':
        command, i = map(int, line.split())
        trains[i] <<= 1
        trains[i] %= (1 << 20)
    elif line[0] == '4':
        command, i= map(int, line.split())
        trains[i] >>= 1

print(len(set(trains[1:])))