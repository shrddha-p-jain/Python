n = int(input("Enter a number: "))
if n<0:
    print("Invalid Input")
else: 
    s=0
    for i in range(1,n+1):
        s = s+(i*i*i)
    print("The sum of cube of first {0} natural numbers is {1}".format(n,s))
