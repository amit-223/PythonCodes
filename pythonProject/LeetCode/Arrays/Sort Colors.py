nums = [2, 0, 2, 1, 1, 0]
cZ = 0
cO = 0
cT = 0
for i in range(len(nums)):
    if nums[i] == 0:
        cZ += 1
    elif nums[i] == 1:
        cO += 1
    else:
        cT += 1
for i in range(cZ):
    nums[i] = 0
for j in range(cZ, cZ + cO):
    nums[j] = 1
for k in range(cZ + cO, cZ + cO + cT):
    nums[k] = 2
print(nums)

print(nums)