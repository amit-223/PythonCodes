import math


def fibformula(n):
    # x = int((math.pow(((1 + math.sqrt(5)) // 2) 2, n)) // math.sqrt(5))
    x = int(math.pow((1 + math.sqrt(5)) // 2), n)

    z = int(y // math.sqrt(5))
    return z


n = 5
print(fibformula(n))
