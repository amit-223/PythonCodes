class Toy:
    def __init__(self, tid, ttype, tprice):
        self.id = tid
        self.toytype = ttype
        self.price = tprice
        self.discount = 0


class Store:
    def __init__(self, toyList, typeList):
        self.toyList = toyList
        self.typeList = typeList

    def fun1(self):
        for i in self.toyList:
            if i.toytype.lower() in self.typeList.keys():
                r = self.typeList[i.toytype.lower()]
                dis = i.price * (r / 100)
                i.discount = dis


if __name__ == '__main__':
    # count = int(input())
    toys = []
    toyTypes = {}
    # for i in range(count):
    id = "104"
    ttype = "Soft Toy"
    price = 1500
    t = Toy(id, ttype.lower(), price)
    toys.append(t)

    # for i in range(3):
    ttype = "Soft Toy"
    amount = 12
    toyTypes[ttype.lower()] = amount
    # input section ends & function calling starts

s = Store(toys, toyTypes)
s.fun1()
s.toyList.sort(key=lambda x: x.discount, reverse=True)
s.toyList.sort(key=lambda x: x.price, reverse=True)

for i in s.toyList:
    dp = i.price - i.discount
    print(i.id, i.price, dp)
