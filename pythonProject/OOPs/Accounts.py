# '''
# int accntNo
# String accntName
# int accntBalance
# '''
#
#
# class Account:
#     def __init__(self, accntNo, accntName, accntBalance):
#         self.accntNo = accntNo
#         self.accntName = accntName
#         self.accntBalance = accntBalance
#
#
# class AccountDemo:
#     def __init__(self):
#         pass
#
#     @classmethod
#     def depositAmnt(cls, l, dep_amount):
#         updated_bal = 0
#         for i in l:
#             updated_bal = i.accntBalance + dep_amount
#         return updated_bal
#
#     @classmethod
#     def withdrawAmnt(cls, l, wid_amount):
#         updated_bal = 0
#         for i in l:
#             updated_bal = i.accntBalance - wid_amount
#         if updated_bal <= 1000:
#             return "No Adequate balance"
#         return updated_bal
#
#
# if __name__ == '__main__':
#     l = []
#     '''
#     120
#     Rajesh
#     1500
#     1200
#     2000'''
#     accntNo = int(input())
#     accntName = input()
#     accntBalance = int(input())
#
#     dep_amount = int(input())
#     wid_amount = int(input())
#
#     l.append(Account(accntNo, accntName, accntBalance))
#
#     ans1 = AccountDemo.depositAmnt(l, dep_amount)
#     print(ans1)
#     ans2 = AccountDemo.withdrawAmnt(l, wid_amount)
#     print(ans2)

class Account:
    def __init__(self, acno, acname, acntbal):
        self.acno = acno
        self.acname = acname
        self.acntbal = acntbal


class AccountDemo:
    def __init__(self):
        pass

    @classmethod
    def depositAmnt(cls, obj, depamnt):
        updated_bal = 0
        updated_bal = obj.acntbal + depamnt
        return updated_bal

    @classmethod
    def withdrawAmnt(cls, obj, withamnt):
        updated_bal = 0
        updated_bal = obj.acntbal - withamnt
        if updated_bal <= 1000:
            return "No Adequate balance"
        return updated_bal


# Sample main section.
# Do not remove the below portion of code.
if __name__ == '__main__':
    acno = int(input())
    acname = input()
    acntbal = int(input())
    depamnt = int(input())
    withamnt = int(input())
    acnt = Account(acno, acname, acntbal)
    acntdemoobj = AccountDemo()
    print(acntdemoobj.depositAmnt(acnt, depamnt))
    print(acntdemoobj.withdrawAmnt(acnt, withamnt))
