items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]]
ruleKey = "type"
ruleValue = "phone"
d = {}
for i in items:
    for j in i:
        if j in d:
            d[j] += 1
        else:
            d[j] = 1

for keys, values in d.items():
    if (keys == ruleValue):
        print(values)

