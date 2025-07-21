nums = input()
half_point = len(nums) // 2

left = 0
right = 0

for i in range(half_point):
  left += int(nums[i])

for i in range(half_point, len(nums)):
  right += int(nums[i])

if left == right:
  print("LUCKY")
else:
  print("READY")