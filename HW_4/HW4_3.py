import os
print(os.getcwd())

l = os.listdir()

file = list()
folder = list()  

for x in l:
    for i in range(len(x)):
        if x[i] == '.':
            file.append(x)
        else:
            folder.append(x)

print('Number of files:',len(file))
print('Number of foldrs:', len(folder))
