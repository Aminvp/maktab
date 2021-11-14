line = input()
d = dict()
while line[-1] != '.':
    line = line + '\n' + input()
for letter in line:
    d[letter] = d.get(letter, 0) + 1
print(d)
