def binary(arr, t, b):
    a = 0
    s = 0
    e = len(arr) - 1



    while (s <= e):
        mid = int(s + e // 2)
        if (t > arr[mid]):
            s = mid + 1

        elif (t < arr[mid]):
            e = mid - 1
        else:
            a = mid

            if (b):

                e = mid - 1

            else:

                s = mid + 1

    return a


def search(arr, t):
    li = []
    x = binary(arr, t, True)
    li.append(x)

    y = binary(arr, t, False)
    li.append(y)
    print(li)


arr = [5, 7, 7, 7, 7, 8, 8]
t = 7
search(arr, t)
