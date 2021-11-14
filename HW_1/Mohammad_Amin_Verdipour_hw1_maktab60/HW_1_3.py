text = input()
d = dict()
while text[-1] != '.':
    text = text + '\n' + input()
for ch in text:
    d[ch] = d.get(ch, 0) + 1
print(d)  

    
    
    
    