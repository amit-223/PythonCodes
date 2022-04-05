def remove(self, s):
    s.lower()
    empty = ""
    for i in s:
        if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
            pass
        else:
            empty += i
    return empty


def small(s):
    # print(min(s)) # e
    l = len(s)
    for i in range(l):
        if (i % 2 == 0):
            print(s[i], end="")


def iterate(str):
    n = 1
    empty = ""
    mid = int(len(str) / 2)
    for i in range(mid - 1, len(str)):
        if (n != 0):
            # print(str[i], end="")
            empty += str[i]
            n = n - 1
    return empty


# s = "hello"
# str = "h"
# ans = iterate(str)
# print(ans)
# small(s)
# ans = remove(s)

def reverse(x):
    l = []
    num = x
    while (num > 0):
        rem = int(x) % 10
        l.append(rem)
        num = int(num) / 10
    return l


# ans = reverse(123)
# for i in ans:
#     print(i, end="")


def xplore(li):
    li2 = []
    m = 0
    for j in li:
        s = j[0].lower()  # take 1st char in a full string
        li2.append(s)
    for k in li2:  # example li2 = ['t','b','t','i','t']
        c = li2.count(k)
        if (c > m):
            m = li2.count(k)
    return m  # here m will 3 because t comes three times


print("str: ")
n = int(input())
li = []
for i in range(n):
    x = input()
    li.append(x)
# li = ["This", "my", "Mere yaara", "This a", "mere y"]
ans = xplore(li)
print(ans)
