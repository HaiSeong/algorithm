n,m,k = map(int, input().split())
nums = sorted(list(map(int, input().split())), reverse=True)
maxNum = nums[0]
secondMaxNum = nums[1]

if m == k:
    print(maxNum * m)
else:
    maxCount = m // k
    secondCount = m % k
    
    print(maxCount * maxNum * k + secondCount * secondMaxNum)
