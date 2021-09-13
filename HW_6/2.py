lst = [1000, 500, 600, 700, 5000, 90000, 175000]
  
def func(x):
    if x < 8000:
        return x + 2000
    else:
        return x

print(list(map(func, lst))) 
    