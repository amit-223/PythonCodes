n = int(input())
l = []
for i in range(n):
    l.append(input())

def is_palindrome(i):
    return i == i[::-1]

for i in l:
     if is_palindrome(i.lower()):
         print(i)
