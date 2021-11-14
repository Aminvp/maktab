import os

adress = input('please enrer adress: ')
files = os.listdir(adress)
for file in files :
    if '.' in file :
        print(file)

print('*' * 50)


for file in files :
    if '.' in file :
        print(file)
        with open(adress+'\\'+file , 'r') as reader :
            print(reader.readline())

            entry = input()
            if entry == "" :
                check = True
                while check == True :
                    print(reader.readline())
                    entry = input()
                    if entry == "" :
                        check = True
                    elif entry == "n" :
                        check = False
                    else :
                        print(reader.readline())
            elif entry == "n" :
                continue
            else :
                print(reader.readline())
            