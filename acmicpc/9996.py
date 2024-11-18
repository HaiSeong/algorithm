
n = int(input())
s = input()
lines = [input() for _ in range(n)]

index_star = s.find('*')


if index_star == 0:
    end = s[1:]
    for line in lines:
        if line.endswith(end):
            print('DA')
        else:
            print('NE')
elif index_star == len(s) - 1:
    start = s[:-1]
    for line in lines:
        if line.startswith(start):
            print('DA')
        else:
            print('NE')
else:
    start = s[:index_star]
    end = s[index_star + 1:]

    for line in lines:
        if len(line) >= len(start) + len(end) and line.startswith(start) and line.endswith(end):
            print('DA')
        else:
            print('NE')

