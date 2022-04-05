class Book:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Library:
    def __init__(self, l_id, address, l):
        self.l_id = l_id
        self.address = address
        self.l = l

    def countbooks(self, char):
        c = 0
        for i in self.l:
            if i.name[0] == char:
                c += 1
        return c

    def removebooks(self, l2):
        for i in l2:
            for j in self.l:
                if i == j.name:
                    self.l.remove(j)


if __name__ == '__main__':
    n = int(input())
    l1 = []
    for i in range(n):
        id = int(input())
        name = input()
        l1.append(Book(id, name))
    char = input()
    m = int(input())
    l2 = []
    for i in range(m):
        l2.append(input())
    l = Library(0, "xyz", l1)
    ans = l.countbooks(char)
    print(ans)
    l.removebooks(l2)
    for i in l.l:
        print(i.name)
