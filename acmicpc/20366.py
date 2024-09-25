n = int(input())
lst = list(map(int, input().split()))

lst.sort()

min_diff = float('inf')
for i in range(n - 1):
    for j in range(i + 1, n):
        left, right = 0, n - 1
        while left < right:
            if left == i or left == j:
                left += 1
                continue
            if right == i or right == j:
                right -= 1
                continue

            height1 = lst[i] + lst[j]
            height2 = lst[left] + lst[right]
            diff = abs(height1 - height2)

            min_diff = min(min_diff, diff)

            if height1 < height2:
                left += 1
            elif height1 > height2:
                right -= 1
            else:
                print(0)  # 완벽히 같은 높이를 찾았을 때
                exit()

print(min_diff)