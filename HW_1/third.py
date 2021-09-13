f = open('abc.txt', 'r')
d = {}

for x in f:
    for i in range(len(x)): 
        if x[i] not in d:
            d[x[i]] = 1
        else:
            d[x[i]] += 1

for x in f:
    for i in range(len(x)):
        d[x[i]] = d.get(x[i], 0) + 1

print(d)

