def printFibb(n):
    # your code here
    arr = []
    arr[1] = arr.append(1)
    arr[2] = arr.append(1)
    for i in range(3, n - 1):
        arr[i] = arr[i - 1] + arr[i - 2]
        arr.append(arr[i])
    return arr


n = 5
res = printFibb(n)
for i in range(len(res)):
    print(res[i])
