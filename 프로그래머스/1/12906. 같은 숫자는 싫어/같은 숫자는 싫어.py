def solution(arr):   
    i = 0 # 탐색
    j = 0 # 저장
    
    while i < len(arr):
        arr[j] = arr[i]
        j += 1
        k = i + 1
        while k < len(arr) and arr[i] == arr[k]:
            k += 1
        i = k
        
    return arr[:j]