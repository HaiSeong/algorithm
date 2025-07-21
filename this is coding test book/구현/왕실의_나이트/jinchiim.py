x, y = str(input())

test = ['a', 'b', 'c', 'd', 'e', 'f', 'h']
can = [(-2, 1), (-2, -1), (2, -1), (2, 1), 
		(1, 2), (1, -2), (-1, 2), (-1, -2) ]

x = test.index(x) + 1
move_count = 0

for i in range(8):
    nx = x + can[i][0]
    ny = int(y) + can[i][1]
    if nx <= 8 and ny <= 8 and nx >= 1 and ny >= 1:
        move_count += 1

print(move_count)