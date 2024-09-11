n = int(input())
lst = list(map(int, input().split()))

# i, j 가 아무리 차이나도 5000 보다 차이가 안남
print(n // 2)

x = 10**6
for i in range(n // 2):
    lst[i] += x
    lst[n - 1 - i] -= x

    print(*lst)
    x -= 5000

