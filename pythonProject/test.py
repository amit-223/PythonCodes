import np as np


def fun(l, length):
    for i in range(length + 1):
        if (i not in l):
            print(i, end=" ")


def fun1(l, length):
    l1 = [];
    for i in range(2, length - 1):
        l1.append(l[i])
    return l1


l = [1, 2, 3, 44, 55, 66, 77]
length = len(l)


# ans = fun1(l, length)
# for x in ans:
#     print(x, end=" ")

def remove(str):
    empty = ""
    x = "cpt"
    for i in str:
        if (i not in x):
            empty += i
    return empty


# NON repeating char in a STRING code
def local(str):
    c = [0] * 256
    for i in str:
        c[ord(i)] += 1
    return c


def nondupli(str):
    c = local(str)
    empty = ""
    for i in str:
        if (c[ord(i)] == 1):
            empty += i
    return empty


str = "karmakar"


# ans = nondupli(str)
# print(ans)


# n = int(input())
# while (n > 0):
#     m = input("Ent")
#     arr = list(map(int, input().split()))
# print(arr)

def t_c(a, b):
    try:
        k = a // b
        print(k)

    except ZeroDivisionError:
        print("Can't divide by zero")


a = 8
b = 4


# t_c(a, b)


class Solution:
    def index_sum(nums, t):
        list = []
        l = len(nums)
        for i in range(0, l - 1):
            for j in range(i, l - 1):
                if (nums[i] + nums[j + 1] == t):
                    list.append(i)
                    list.append(j + 1)
        return list


nums = [3, 3]
x = nums[1:2]
# print(x)
t = 6
obj = Solution
# ans = obj.index_sum(nums, t)
# print(ans)

str1 = 'Do not give up, starting is always toughest'
# str1[:2] + 'nit' + ' ' + str1[6:]
# print(str1[:35] + "hardest")

A = '1234567'
# print(A[1::2])
Name = "Michael Jackson"
# print(Name.upper())
# print(Name.find('el'))
a = '1'
b = '2'
# print(a + b)
tuple1 = ("A", "B", "C")
# print(tuple1[-1])
A = ((11, 12), [21, 22])
# print( A[1])
# print( '1,2,3,4'.split(','))
A = [1, 'a']
B = [2, 1, 'd']
# print(A + B)
V = {'A', 'B'}
# print( V.add('C'))
A = ['1', '2', '3']

# for a in A:
# print(2 * a)
name = '01234567'
# print(name[::2])
a = np.array([0, 1, 0, 1, 0])

b = np.array([1, 0, 1, 0, 1])

print(a * b)
