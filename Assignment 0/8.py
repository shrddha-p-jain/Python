n = int(input("Enter a number: "))

if n<=0:
    print("Error: Must enter a positive number")
else:
    b=1
    c=0
    a=0
    for i in range(2,n+1):
        
        a=b
        b=c
        c=a+b
    print("{}th fibonacci number is: {}".format(n,c))
