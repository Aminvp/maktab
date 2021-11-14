import math

class Shape:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        print(f'area:{self.width * self.length}')
    
    def circumference(self):
        print(f'circumference:{2 * (self.width + self.length)}')
    
    def show(self):
        for i in range(self.width):
            for j in range(self.length):
                print("*", end='')
            print()
    

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(length, width)
        
   
class Square(Shape):
    def __init__(self, a):
        super().__init__(length=a, width=a)
    

class Parallelogram(Shape):
    def __init__(self, b, h):
        super().__init__(length=b, width=h)
    
    def circumference(self):
        print(f'circumference : {2 * (self.length + math.sqrt(self.length ** 2 + self.width ** 2))}')
    
    def show(self):
        for i in range(self.width):
            for j in range(self.length - i):
                print(' ',end='')
            for j in range(self.length):
                print('*', end='')
            print()    
        
        
class Rhombus(Shape):
    def __init__(self, w):
        super().__init__(length=w, width=w/math.sqrt(2)) 
    
    def circumference(self):
        print(f'circumference : {4 * self.length}')

    def show(self):
        for i in range(round(self.width)):
            for j in range(self.length - i):
                print(' ',end='')
            for j in range(self.length):
                print('*', end='')
            print()        


class Diamond(Shape):
    def __init__(self, w):
        super().__init__(length = w, width = w)
      
    def show(self):
        d = int(self.length * math.sqrt(2)//2)
        for i in range(d):
            print(' ' * (d-i-1), '*' * (2*i - 1))
        for i in reversed(range(d)):
            print(' ' * (d-i-1), '*' * (2*i - 1))
    
            
print('for Rectangle:')     
ob = Rectangle(4, 2)
ob.area()
ob.circumference()
ob.show()
print('--------------')      

print('for Square:')    
ob1 = Square(3)
ob1.area()
ob1.circumference()
ob1.show()
print('--------------')  

print('for Parallelogram:')
ob2 = Parallelogram(4, 3)
ob2.area()
ob2.circumference()
ob2.show()
print('--------------') 

print('for Rhombus:')
ob3 = Rhombus(5)
ob3.area()
ob3.circumference()
ob3.show() 
print('--------------') 

print('for Diamond:')
ob4 = Diamond(8)
ob4.area()
ob4.circumference()
ob4.show()
print('--------------') 
















