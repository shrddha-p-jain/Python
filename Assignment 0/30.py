x=int(input("enter a year:"))
if(x<=0):
    print("invalid entry")
else:
    if(x%4==0):
        if(x%100==0):
            if(x%400==0):
                print(x, " is leap year")
            else:
                print(x, "is not a leap year")
        else:
            print(x, " is a leap year")
    else:
        print(x, "is not a leap year")

