
while True:
    line = input()
    if line == '0':
        break
    n, a, b = map(int, line.split())

    visited = {}
    order = 1
    x = 0
    visited[0] = 1
    while True:
        order += 1
        next = (a * x * x + b) % n
        if next in visited:
            print(n - (order - visited[next]))
            break
        visited[next] = order
        x = next

