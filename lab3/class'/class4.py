class Point:
    def __init__(self, x, y):#for inicialization of variables
        self.x = x
        self.y = y

    def move(self): 
        self.x = int(input())#to input from keyboard
        self.y = int(input())

    def show(self):
        print('(',self.x,';',self.y,')')#outputing vivodit

    def dist(self):
        self.a = int(input())#for input coordinates
        self.b = int(input())
        k = (((self.x - self.a) ** 2) + ((self.y - self.b) ** 2))#finding distance
        print (k ** (0.5))
x = int(input())
y = int(input())
a = Point(x, y)
a.show()
a.move()
a.show()
a.dist()