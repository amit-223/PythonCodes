# num = int(input())
# while (num != 0):
#     rem = num % 10
#     print(rem, end="")
#     num = int(num / 10)


def increment(x):
    x += 4
    return x


x = 5
ans = increment(x)
print(ans)
