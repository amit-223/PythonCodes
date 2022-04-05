n = 1
ch = '5'
if (ch in ('@', '_', '!', '#', '$', '%', '^', '&', '*', '(', ')', '<', '>', '?', '/', '|', '}', '{', '~', ':')):

    lst = ['hello']
    # for i in range(0, n):
    #     lst.append(input())

    for i in lst:
        c = 0
        res = ""
        for j in i:
            if (j.lower() in ('a', 'e', 'i', 'o', 'u', ch)):
                c += 1
                res += ch
            else:
                res += j

        print(res, c)
else:
    print("Not a Special Character")
