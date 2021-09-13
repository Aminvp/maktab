class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def getPerimeter(self):
        return (self.length + self.width) * 2

    def getArea(self):
        return self.width * self.length

    def draw(self):
        for i in range(self.width):
            for j in range(self.length):
                if j == 0 or j == self.length - 1 or i == 0 or i == self.width - 1:
                    print('*', end='  ')
                else:
                    print(' ', end='  ')
            print()

    def show(self):
        area = self.getArea()
        perimeter = self.getPerimeter()
        print(f'length : {self.length} , width : {self.width} , perimeter : {perimeter} , area : {area}')
        self.draw()


r = Rectangle(int(input()), int(input()))
r.show()
