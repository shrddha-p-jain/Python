sum = 0
num = 0
while True:
    x = int(input("Enter next number, or 0 to finish:"))
    if x==0:
        break
    sum+=x
    num+=1
print('the sum of the given numbers is %.2f and the average is %.2f'%(sum,sum/num))    
