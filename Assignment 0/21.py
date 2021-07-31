x,y,z=input("enter 3 sides of a triangle").split()
x = int(x)
y=int(y)
z=int(z)
if(x>0 and y>0 and z>0):
    triangle="scalene"
    if(x==y or y==z or x==z):
        if(x==y==z):
            triangle="equilateral"
        else:
            triangle="isoceles"
    print("The triangle is",triangle)
else:
    print("Sides cannot be negative")
