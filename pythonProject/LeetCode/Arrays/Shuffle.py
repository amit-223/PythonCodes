nums = [2, 5, 1, 3, 4, 7]
n = 3
arr = []
j = 0
mid = n
for i in range(1, n):
    arr[j].append(nums[i])
    arr[j + 1].append(nums[mid + 1])
    j += 2
    mid += 1

for i in arr:
    print(i)
