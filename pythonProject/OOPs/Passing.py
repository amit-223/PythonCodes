class A:
    def __init__(self, x, y):
        self.x = x  # instance variable
        self.y = y


class B:
    @classmethod
    def print(cls, s1, s2, num, num2):
        # for i in list:
        #     if i.x == num:
        #         return num
        # return "No"
        if s1 == num:
            return num


if __name__ == '__main__':
    x = 5
    y = 6
    # here we r append into list first & after pass to the
    # another class arguments...
    # l = []
    # l.append(A(x, y))
    # print(B.print(l, 5))

    # & here first we create object of each instance variable
    # then pass into arguments
    obj = A(x, y)
    s1 = obj.x
    s2 = obj.y
    print(B.print(s1, s2, 5, 6))
