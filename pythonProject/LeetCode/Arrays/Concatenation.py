def conc(nums):
    n = len(nums)
    array = []
    for i in range(n):
        array[i].append(nums[i])
        array[i + n].append(nums[i])
    return array


nums = [1, 2, 1]
conc(nums)
