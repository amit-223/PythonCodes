nums = [12, 345, 2, 6, 7896]
c = 0
for i in nums:
    count = 0
    while (i != 0):
        rem = i % 10
        count += 1
        i = i // 10

    if count % 2 == 0:
        c += 1

# print(c)
