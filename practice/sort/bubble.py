from random import randint

arr = [randint(0, 10) for _ in range(10)]

for i in range(len(arr) - 1, 0, -1):
    for j in range(i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr)

