# code
def reverse(arr):
    arr.reverse()


print("Ent")
T = int(input())
l = []
while (T != 0):
    print("ele")
    N = int(input())
    # l = list(map(int, input().split()))
    arr = []
    while (N != 0):
        li = int(input())
        arr.append(li)
        N = N - 1
    T = T - 1

    # for i in range(N):
    #     print("in arr")
    #     A = int(input())
    #     l.append(A)
reverse(arr)
for e in arr:
    print(e, end=" ")
