mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

sum = 0

for i in range (len(mat)):
    for j in range(len(mat[i])):
        if i == j or i + j == len(mat) - 1:
            sum += mat[i][j]
print(sum)
