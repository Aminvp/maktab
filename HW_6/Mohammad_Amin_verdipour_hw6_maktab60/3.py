lst = [-1000, 500, -600, 700, 5000, -90000, -175000]
lst_2 = list()

def func(x):
    if x < 0:
        return True
    else:
        return False

result = filter(func, lst)

for item in result:
    lst_2.append(abs(item)) 

print(lst_2)
