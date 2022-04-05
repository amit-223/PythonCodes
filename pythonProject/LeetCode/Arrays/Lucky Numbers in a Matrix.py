matrix = [[3, 7, 8], [9, 11, 13], [15, 16, 17]]
maximum = 0
for i in matrix:
    minimum = min(i)
    if minimum > maximum:
        maximum = minimum
# print(maximum)

minrow = {min(r) for r in matrix}
maxcol = {max(c) for c in zip(*matrix)}
print(list(minrow & maxcol))
