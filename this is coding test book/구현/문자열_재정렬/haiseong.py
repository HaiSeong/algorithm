
line = list(input())

line.sort()

num = 0
for c in line:
    if '0' <= c <= '9':
        num += int(c)
    else:
        print(c, end='')
print(num)