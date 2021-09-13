import os
print(os.getcwd())

os.chdir('C:\\Users\\AMIN_vp\\Desktop\\New folder')

print(os.getcwd())

lst = os.listdir()

for x in lst:
    with open(x) as reader, open('save.txt', 'w') as writer:
        for line in reader:
            writer.write(line)



        
        
    
        
       

    
