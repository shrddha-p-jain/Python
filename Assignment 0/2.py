
p=float(input("enter principle amount: "))
r=float(input("enter rate of interest: "))
t=float(input("enter time period: "))
def SI(p,r,t):
      return (p*r*t)/100
if(p<0 or r<0 or t<0):
    print("inputs not valid. Enter values greater than zero")
else:
    print("Simple interest: %.02f "%SI(p,r,t))
