class Student:
    def __init__(self, age, height, weight):
        self.age = age
        self.height = height
        self.weight = weight


class School:
    def __init__(self, studentsNum):
        self.studentsNum = studentsNum
        self.studentsList = list()

    def addStudent(self, student):
        self.studentsList.append(student)

    def getHeightAvr(self):
        result = list(map(lambda x: x.height, self.studentsList))
        result = sum(result) / len(result)
        return result

    def getWeightAvr(self):
        result = list(map(lambda x: x.weight, self.studentsList))
        result = sum(result) / len(result)
        return result

    def getAgeAvr(self):
        result = list(map(lambda x: x.age, self.studentsList))
        result = sum(result) / len(result)
        return result


n = int(input())
A = School(n)
ages = list(map(int, input().split()))
heights = list(map(int, input().split()))
weights = list(map(int, input().split()))
for i in range(0, n):
    A.addStudent(Student(ages[i], heights[i], weights[i]))
n = int(input())
B = School(n)
ages = list(map(int, input().split()))
heights = list(map(int, input().split()))
weights = list(map(int, input().split()))
for i in range(0, n):
    B.addStudent(Student(ages[i], heights[i], weights[i]))
print(A.getAgeAvr())
heightAvr1 = A.getHeightAvr()
print(heightAvr1)
weightAvr1 = A.getWeightAvr()
print(weightAvr1)
print(B.getAgeAvr())
heightAvr2 = B.getHeightAvr()
print(heightAvr2)
weightAvr2 = B.getWeightAvr()
print(weightAvr2)
if heightAvr2 > heightAvr1:
    print('B')
elif heightAvr1 > heightAvr2:
    print('A')
elif weightAvr2 > weightAvr1:
    print('A')
elif weightAvr2 < weightAvr1:
    print('B')
else:
    print('Same')
