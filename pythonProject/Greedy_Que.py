def find_max(a1, a2, a3):
    sum = 0
    mx3 = max(a3)
    sum += mx3

    a2.sort()
    n = len(a2) - 1
    while (n >= 0):
        if (a2[n] < mx3):
            sum += a2[n]
            mx2 = a2[n]
            break
        n = n - 1

    a1.sort()
    m = len(a1) - 1
    while (m >= 0):
        if (a2[m] < mx2):
            sum += a2[n]
            break
        m = m - 1

    ''' mx2 = max(a2)
    if mx2 < mx3:
        sum += mx2
    else:
    mx1 = max(a1)
    if mx1 < mx2:
        sum += mx1
    else:
        return 0         return 0 '''

    return sum


a1 = [1, 7, 3, 4]
a2 = [4, 2, 5, 1]
a3 = [9, 5, 1, 8]


# a1 = [7, 8, 9]
# a2 = [4, 5, 6]
# a3 = [3, 2, 1]
# ans = find_max(a1, a2, a3)
# print(ans)


def balanced_str(s):
    if len(s) == 0:
        return 0
    count = 0
    l = 0
    n = len(s)
    for i in range(n):
        if s[i] == "L":
            l += 1
        else:
            l -= 1
        if l == 0:
            count += 1
    return count


s = "RLRRLLRLRL"


# ans = balanced_str(s)
# print(ans)


def maximum69Number(num):
    num = str(num)
    for i in range(len(num)):
        if num[i] == "6":
            return num[:i] + "9" + num[i + 1:]
    return num


num = 9999


# ans = maximum69Number(num)
# print(ans)


def minOperations(n):
    count = 0
    for i in range(len(n) - 1):
        if n[i] < n[i + 1]:
            while n[i + 1] == n[i] + 1:
                n[i] = n[i] + 1
                count += 1
        else:
            while n[i] >= n[i + 1]:
                n[i + 1] = n[i + 1] + 1
                count += 1
    return count


n = [1]


# ans = minOperations(n)
# print(ans)


def pairCount(numb):
    c = 0
    for i in range(len(numb) - 1):
        for j in range(i + 1, len(numb)):
            c += 1
    return c


li = [2,1,4,5,7,9]
ans = pairCount(li)
print(ans)
