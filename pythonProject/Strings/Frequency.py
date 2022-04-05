str = "aaaammmiit"
# Method 1
all_frequency = {}
for i in str:
    if i in all_frequency:
        all_frequency[i] += 1
    else:
        all_frequency[i] = 1
# print(all_frequency)

# Method 2
empty = ""
for i in str:
    if i not in empty:
        empty += i
for j in empty:
    c = str.count(j)
    print('{} = {}'.format(j, c))
