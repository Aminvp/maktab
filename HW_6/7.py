def only_even_parameters(func):
    def wrapper(a, b):
        try:
            if a % 2 == 0 and b % 2 == 0 :
                return func(a, b)
            else:
                return "please only use even numbers!" 
        except Exception as ex:    
            return ex  
    return wrapper




@only_even_parameters
def myFunction(a, b): 
     return a+b

print(myFunction(5, 5))

print(myFunction(4, 4)) 

print(myFunction('a', 'b'))
    
print(myFunction(4, 5))