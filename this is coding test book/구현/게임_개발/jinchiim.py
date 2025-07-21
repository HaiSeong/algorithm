n, m = map(int, input().split())
x, y, d = map(int, input().split())

array = []
for i in range (n):
    array.append(list(map(int, input().split())))
    
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
direction = [0, 1, 2, 3]
n_direction = [3, 0, 1, 2]

turned = 0
count = 0

while True:
    
    d = n_direction[direction.index(d)]
    
    nx = x + dx[d]
    ny = y + dy[d]
    # 이동  못한다면 위치는 그대로여야 하므로, nx 변수 사용

    if array[nx][ny] == 0:
        array[nx][ny] = 1
        x, y = nx, ny
        turned = 0 
        count += 1
        continue
        # 진행했으나 가보지 않은 칸
    
    else:
        # 진행했으나 가본 칸이거나 바다이거나 판을 넘는다면
        turned += 1
    
    if turned == 4:
        # 전체 방향이 갈 수 없다면..
        nx = x - dx[d]
        ny = y - dy[d]    
        # 제자리로 돌아온 후
        
        if array[nx][ny] == 0:
            turned = 0
            x, y = nx, ny        
        else:
            break  
            
print(count)