
n=int(input("Enter a number: "))
if(n<1):
    print("invalid input")
elif(n==1):
    print(n, " is not prime")
else:
    for i in range(2,n//2+1):
        if(n%i==0):
            print("{0} is not prime".format(n))
            break
    else:
        print("{0} is prime".format(n))
