
line = input()
right, left = line[:len(line) // 2], line[len(line) // 2:]

if sum(map(int, list(right))) == sum(map(int, list(left))):
    print("LUCKY")
else:
    print("READY")
