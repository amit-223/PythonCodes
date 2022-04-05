str = ["almost", "vtyw"]
vowel = ['a', 'e', 'i', 'o', 'u']
ans=[]

for i in str:
    v = 0
    c = 0
    for j in i:
        if j.lower() in vowel:
            v+=1
        else:
            c+=1
    if c == len(i):
        ans.append(i)

print(ans)