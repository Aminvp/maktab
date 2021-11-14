class Student:
    def __init__(self):
        self.n = int(input('number:'))
        self.h = [int(input('height:')) for i in range(self.n)]
        self.w = [int(input('weight:')) for i in range(self.n)]
        self.a = [int(input('age:')) for i in range(self.n)]
    
    def average_h(self):
        print(sum(self.h) / self.n)
    
    def average_w(self):
        print(sum(self.w) / self.n)
    
    def average_a(self):
        print(sum(self.a) / self.n)
    
    
            
            
A = Student()
B = Student()

A.average_a()
A.average_h()
A.average_w()

B.average_a()
B.average_h()
B.average_w()

