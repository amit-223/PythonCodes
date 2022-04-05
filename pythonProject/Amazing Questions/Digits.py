'''Q1. Problem statement:
Given two non-negative integers n1 and n2, where n1 <n2. The task is to find the total number of integers
in the range interval [n1, n2] [both inclusive] which have no repeated digits.
For e.g.
Suppose n = 11 and m = 15.
There is the number 11, which has repeated digits, but 12, 13, 14, and 15 have no repeated digits. So, the
output is 4.
I '''

# n = 101
# m = 200
n = int(input())
m = int(input())
c = 0
for i in range(n, m + 1):
    l = []
    temp = i
    while temp > 0:
        rem = temp % 10
        l.append(rem)
        temp //= 10
    if len(l) != len(set(l)):
        pass
    else:
        c += 1
if c == 0:
    print("No number found")
else:
    print(c)
