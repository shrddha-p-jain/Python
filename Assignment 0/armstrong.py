x=input("enter number")
l=len(x) #input takesinput in string, convert if needed

s=0
for y in x:
    y1=int (y)
    s+=pow(y1,l)
if s==int(x): # because x is in string
    print("{0} is an armstrong number".format(x))
else:
    print("{0} is not an armstrong number".format(x))
