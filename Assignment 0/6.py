r = float(input("Enter the radius: "))
if r<=0:
    print("Radius cannot be less than zero")
else:
    area = (22/7)*r*r
    print("The area of circle with radius %.2f is %.2f"%(r,area))
