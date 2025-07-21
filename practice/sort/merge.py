
def merge_sort(arr):
    length = len(arr)
    if length <= 1:
        return arr

    sorted_arr = []
    left = merge_sort(arr[:length//2])
    right = merge_sort(arr[length//2:])

    i,j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    while i < len(left):
        sorted_arr.append(left[i])
        i += 1
    while j < len(right):
        sorted_arr.append(right[j])
        j += 1

    return sorted_arr

print(merge_sort([3,5,61,1,1,3,4,7,2,9,985,42,34,567,7,6543,212,6,76,54321,345,65,4321,2345,65432]))
