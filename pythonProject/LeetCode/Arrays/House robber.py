nums = [1, 3]

n = len(nums)

# def fun(nums, n):
#     if n == 1:
#         return nums[n - 1]
#     elif n == 2:
#         return max(nums)
#     else:
s = 0
s2 = 0
for i in range(n):
    if i % 2 == 0:
        s += nums[i]
    else:
        s2 += nums[i]

print(max(s, s2))
# return s
#
# print(fun(nums, n))
