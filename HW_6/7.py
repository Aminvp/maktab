def only_even_parameters(func):
    def wrapper(*args):
        try:
            for x in args:
                if x % 2 == 0:
                    return func(*args)
        except Exception as ex:    
            return ex  
        else:
            return "please only use even numbers!" 
    return wrapper




@only_even_parameters
def myFunction(a, b): 
     return a+b

print(myFunction(5, 5))

print(myFunction(4, 4)) 
    