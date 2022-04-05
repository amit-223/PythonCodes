nums = [2, 3, 5, 1, 3]
m = max(nums)
n = len(nums)
extra = 3
ex = 3
arr = []
for i in nums:
    num = i + ex
    if (num >= n):
        arr.append(True)
    else:
        arr.append(False)

print(arr)
