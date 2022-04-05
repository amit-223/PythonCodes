nums = [3,4,-1,1]
temp = nums[0]
for i in range(1, len(nums)):
    if nums[i] < temp:
        temp = nums[i]
print(nums.index(temp) + 1)