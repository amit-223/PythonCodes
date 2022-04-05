class Employee:
    def __init__(self, eid, ename, erole, esalary):
        self.eid = eid
        self.ename = ename
        self.erole = erole
        self.esalary = esalary

    def increasesalary(self, percent):
        self.esalary += self.esalary * percent * 0.01


class Organization:
    def __init__(self, orgname, l):
        self.orgname = orgname
        self.l = l

    def calculateincrement(self, role, percent):
        l2 = []
        for i in self.l:
            if i.erole == role:
                i.increasesalary(percent)
                l2.append(i)
        return l2


if __name__ == '__main__':
    n = int(input())
    l = []
    for i in range(n):
        eid = int(input())
        ename = input()
        erole = input()
        esalary = int(input())
        l.append(Employee(eid, ename, erole, esalary))
        obj = Organization("xyz", l)
        inprole = input()
        percent = int(input())
        ans = obj.calculateincrement(inprole, percent)
        if len(ans) != 0:
            for i in ans:
                print(i.ename, '\t', i.esalary)
        else:
            print("No")
