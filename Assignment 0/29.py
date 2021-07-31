
def mean(arr):
    sum1 = 0
    count = 0
    for i in arr:
        sum1 = sum1+int(i)
        count+=1
    return(sum1/count)
def median(arr):
    arr.sort()
    l=len(arr)
    if l%2!=0:
        return int(arr[(l+1)//2-1])
    else:
        return (int(arr[l//2-1])+int(arr[l//2]))/2
def mode(arr):
    mean1=float(mean(arr))
    median1 = int(median(arr))
    mode = 3*median1-2*mean1
    return mode   
       

inp = input("Enter the numbers separated by space separated by space: ").split(" ")

print(inp)
print("Mean: {}\n Median: {} \n Mode: {}".format(mean(inp),median(inp),mode(inp)))

'''
sum1=0
l=0
for i in inp:
    sum1 = sum1+int(i)
    l = l+1

if l%2!=0:
    median = int(inp[(l+1)//2])
else:
    median= int((inp[l//2]+inp[l//2+1])/2)

mean = sum1/l


mode = 3*median-2*mean
    
print(mean,median,mode)

'''
