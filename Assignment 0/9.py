def sum_square(n):
    s=0
    for i in range(1,n+1):
        s = s+(i*i)
    return s

x = int(input("Enter a number: "))
if x<=0:
    print("Not a valid input")
else:
    sum_sq = sum_square(x)
    print("The sum of squares of first {0} natural numbers is {1}".format(x,sum_sq))        
