choice=int(input("choose 1 for F to C\n2 for C to F: "))

if (choice==1):
    f=float(input("enter temperature in F: "))    
    c=(f-32)*5/9
    print("Celcius temp is %.02f"%(c))
elif(choice==2):
    c=float(input("enter temperature in C: "))  
    f=(9*c)/5+32
    print("Farenheit temp is %.02f"%f)
else:
    print("invalid choice")
