import math
def areaSquare(x):
    area = x**2
    xWedge = x/2
    totalArea = area - xWedge
    print("the total area is ", totalArea)

areaSquare(10)

##def areaOfWedges(diameter,length):
##    squareArea= length**2
##    radius = diameter/2
##    circleArea= math.pi * radius

def area(x):
    x=float(input("side of the square "))
    areaSquare = x**2
    areaCircle = math.pi*(x/2)**2
    a = areaSquare - areaCircle
    print(a)

