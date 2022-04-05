def demo(s):
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    c = 0
    for value in d.values():
        c += 1

    if (c == 26):
        return True

s = "thequickbrownfoxjumpsoverthelazydog"
demo(s)

    # if (value < 2):
    #     print("f")
    # else:
    #     print("t")
