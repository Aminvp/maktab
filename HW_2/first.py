class Student:
    def __init__(self):
        self.number = 0
        self.age = []
        self.weight = []
        self.height = []
        
    def getinfo(self):
        self.number = int(input("number of students:"))
        self.age = list(map(int, input("enter age:").split()))
        self.weight = list(map(int, input("enter weight:").split()))
        self.height = list(map(int, input("enter height:").split()))
        return self.number, self.age, self.weight, self.height

class School:
    def __init__(self):
        self.sum = 0
        self.avgage = 0
        self.avgweight = 0
        self.avgheight = 0
    
    def calculate(self):
        c = Student()
        number, age, weight, height = c.getinfo()
        self.avgage = sum(age) / number
        self.avgweight = sum(weight) / number
        self.avgheight = sum(height) / number 
    
    def show(self):
        print(self.avgage)
        print(self.avgweight)
        print(self.avgheight)
    
    def compare(self, self2):
        if self.avgheight > self2.avgheight:
            print("A")
        elif self.avgheight < self2.avgheight:
            print("B")
        elif self.avgweight > self2.avgweight:
            print("B")
        elif self.avgweight < self2.avgweight:
            print("A")
        else:
            print("same")

A = School()
B = School()
A.calculate()
B.calculate()
A.show()
B.show()
A.compare(B) 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    