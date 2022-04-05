nums = [1, 2, 3, 4]
p = 1
n = len(nums)
output = []
for i in range(0, n):
    output.append(p)
    p = p * nums[i]
p = 1
print(output)
for i in range(n - 1, -1, -1):
    output[i] = output[i] * p
    p = p * nums[i]
print(output)

#     for j in range (len(nums)):
#         if i != j:
#             p = p * nums[j]
#     ans.append(p)
# print(ans)
