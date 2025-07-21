nums = list(map(int, list(input())))

answer = nums[0]

for n in nums[1:]:
    answer = max(answer + n, answer * n)

print(answer)
