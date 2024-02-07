import math

def sphere_volume(radius):
    if radius < 0:
        return "Radius cannot be negative."
    
    volume = (4/3) * math.pi * radius**3
    return volume

radius = int(input())
print(sphere_volume(radius))