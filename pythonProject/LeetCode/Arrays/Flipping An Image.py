image = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
for i in range(len(image)):
    image[i].reverse()
    for j in range(len(image[i])):
        if image[i][j] == 0:
            image[i][j] = 1
        else:
            image[i][j] = 0
print(image)



# [[1,0,0],[0,1,0],[1,1,1]]
