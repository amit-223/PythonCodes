def Arr_returning(nums):
    arr = []
    for i in range(5):
        arr.append(i)
    return arr
    # return nums


nums = [1, 2, 3]
ans = Arr_returning(nums)
for i in ans:
    print(i)
