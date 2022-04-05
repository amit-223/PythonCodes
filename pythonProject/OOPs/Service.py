# Asked in 20-March-2022
class Service:
    def __init__(self, id, name, manufacturer, distance, isInsured):
        self.id = id
        self.name = name
        self.manufacturer = manufacturer
        self.distance = distance
        self.isInsured = isInsured
        self.minpay = 0


class ServiceCenter:
    def __init__(self, l, d):
        self.l = l
        self.d = d
        for i in l:
            if i.isInsured == "yes":
                i.minpay = 1000
            else:
                i.minpay = 1750

    def meth(self, code):
        res = []
        for i in self.l:
            if i.distance > 5000 and d.values()==code:
                res.append(i.id)
                res.append(i.name)
                res.append(i.manufacturer)
                res.append(i.minpay)
                return res
            else:
                return None


if __name__ == '__main__':
    n = int(input())
    l = []
    d={}
    for i in range(n):
        id = int(input())
        name = input()
        manufacturer = input()
        distance = int(input())
        isInsured = input()
        l.append(Service(id, name, manufacturer, distance, isInsured))
        d[id] = input()
        obj=ServiceCenter(l,d)
        ans=obj.meth(d[id])
        for i in ans:
            print(i)
'''
4
101
tata
Baleno
7300
yes
KA
102
Honda
City
700
no
KL
103
Tata
Safari
6000
No
KA


'''