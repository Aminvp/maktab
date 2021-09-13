import math

class Sphere:
    def __init__(self, radius):
        self.radius = radius
        if self.radius <= 0:
            try:
                self.radius = abs(self.radius)
            except:
                print('error')
    
    def area(self):
        print (f'area is Sphere : {4 * math.pi * self.radius * self.radius}')

    def volume(self):
        print (f'volume is Sphere : {4/3 * math.pi * self.radius * self.radius * self.radius}')  

    
ob = Sphere(-4)
ob.area()
ob.volume()