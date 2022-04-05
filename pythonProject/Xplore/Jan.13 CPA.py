str1 = "I am good"
str2 = "Who am I"


def fun1(str1, str2):
    for i in str1:
        if i not in str2:
            return False
    return True


if fun1(str1.lower(), str2.lower()):
    print("Valid")
else:
    print("Not valid")
print(str1)
