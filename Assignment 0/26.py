str1=input("enter string")
num=0
alph=0
for char in str1:
    if char in("0123456789"):
        num+=1
    if char in("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        alph+=1
print("number of alphabets: {} \n number of numbers: {}".format(alph,num))
    
