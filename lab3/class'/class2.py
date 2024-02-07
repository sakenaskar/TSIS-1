class Shape:
    def area1(self):
        print(0)

class Square(Shape):
    def __init__(self,length):
        self.length = length
    
    def area2(self):
        print(self.length * self.length)

x = int(input())
a = Square(x)
a.area1()
a.area2()