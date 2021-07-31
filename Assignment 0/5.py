start=int(input("Enter first number: "))
end=int(input("Enter last number: "))
if(start>end or start<1 or end<1):
    print("invalid entry")
else:
    flag=0
    if(start==1):
        start+=1
    for i in range(start,end+1):
        for x in range(2,i//2):
            if(i%x==0):
                break
        else:
            flag = 1
            print(i)
    if flag==0:
        print("no prime numbers between given range")

    
