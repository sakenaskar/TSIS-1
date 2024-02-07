class Shape:
    def area1(self):
        print(0)

class Rectangle(Shape):
    def __init__(self, length,width):
        self.length = length
        self.width = width

    def area2(self):
        print(self.length * self.width)

x = int(input())
y = int(input())
a = Rectangle(x, y)
a.area1()
a.area2()