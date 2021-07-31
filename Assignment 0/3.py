x = input("enter a number: ")
l = len(x)
x1 = int(x)
s = 0
for y in x:
    s+=pow(int(y),l)

if s==x1:
    print("{0} is an armstrong number".format(x1))
else:
    print("{0} is not an armstrong number".format(x1))

