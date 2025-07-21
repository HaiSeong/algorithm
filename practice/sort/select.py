import random

arr = [random.randint(1, 10) for _ in range(10)]
n = 10

for i in range(n - 1):
    min_idx = i
    for j in range(i + 1, n):
        if arr[min_idx] > arr[j]:
            min_idx = j
    arr[min_idx], arr[i] = arr[i], arr[min_idx]

print(arr)