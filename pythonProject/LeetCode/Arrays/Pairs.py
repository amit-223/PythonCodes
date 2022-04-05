nums = [1, 1, 1, 1]
n = len(nums)
c = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if (nums[i] == nums[j]):
            c += 1
print(c)
