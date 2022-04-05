# Method 1
str = "infosys"
n = len(str) - 1
while (n >= 0):
    print(str[n], end="")
    n = n - 1
print()
#OR (recommanded)
for i in range(len(str) - 1, -1, -1):
    print(str[i],end="")

# Method 2
# Not recommanded (Bakwas Method)
str1 = "infosys"
l = []
for i in str1:
    l.append(i)
# for j in range(len(l) - 1,-1, -1):
#     print(str[j], end="")



