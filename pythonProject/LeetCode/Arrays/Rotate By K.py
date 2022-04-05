nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

while k != 0:
    n = len(nums) - 1
    temp = nums[n]
    for i in range(n, 0, -1):
        nums[i] = nums[i - 1]
    nums[0] = temp
    k -= 1

print(nums)
