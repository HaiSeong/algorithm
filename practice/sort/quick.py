def quick_sort(arr, start, end):

    pivot = start
    left = start + 1
    right = end

    if left >= right:
        return

    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right >= start + 1 and arr[right] >= arr[pivot]:
            right -= 1

        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
        else:
            arr[pivot], arr[right] = arr[right], arr[pivot]
            pivot = right

    quick_sort(arr, start, pivot - 1)
    quick_sort(arr, pivot + 1, end)

arr = [1,3,4,45,123,4,6,71 ,1,2,2,34,1,234,5,161,1]

quick_sort(arr, 0, len(arr) - 1)

print(arr)

