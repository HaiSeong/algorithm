import random

n = 10000
arr = [random.randint(1, 10000) for _ in range(n)]

print(arr)

for i in range(1, n):
    key = arr[i]
    j = i - 1
    while j >= 0:
        if arr[j] <= key:
            break
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key


print(arr)



