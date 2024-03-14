import math

def ctg(rad):
    return 1 / math.tan(rad)

n = float(input("Input number of sides: "))
a = float(input("Input the length of a side: "))

grad = 180/n
rad = grad*(math.pi/180)
cot = ctg(rad)

S = int((n * pow(a, 2) * cot)/4)
print("The area of the polygon is:", S)