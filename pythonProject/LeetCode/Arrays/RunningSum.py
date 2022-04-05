def sum(nums):
    n = len(nums)
    for i in range(1, n):
        nums[i] = nums[i - 1] + nums[i]
    return nums


nums = [1, 1, 1, 1]
print(sum(nums))
