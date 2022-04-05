def inverse_pyra(n):
    for i in range(n, 0, -1):
        for j in range(1, i + 1,1):
            print("*", end="")
        print()


n = 4
inverse_pyra(n)
