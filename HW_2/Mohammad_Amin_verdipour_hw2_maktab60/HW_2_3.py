import turtle as t

class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length
        self.area = self.area()
        self.environment = self.environment()
    
    def shape(self):
        s = t.getscreen()
        t.fd(self.length * 100)
        t.left(90)
        t.fd(self.width * 100)
        t.left(90)
        t.fd(self.length * 100)
        t.left(90)
        t.fd(self.width * 100)
        return s
                
        
        
    def area(self):
        return self.width * self.length
    
    def environment(self):
        return (2 * (self.width + self.length))
    
    def show(self):
        print(self.length)
        print(self.width)
        print(self.area)
        print(self.environment)
        

A = Rectangle(2, 3)
A.shape()
print()
A.show()
