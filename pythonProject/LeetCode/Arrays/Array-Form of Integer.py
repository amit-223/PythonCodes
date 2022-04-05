num = [2, 1, 5]
num1 = [2, 1, 5]
k = 806
a = 0
l = []
for i in num:
    a = 10 * a + i

ans = a + k

while ans != 0:
    rem = ans % 10
    l.append(rem)
    ans //= 10

for i in range(len(l) - 1, -1, -1): # reverse array printing
    print(l[i],end="")
