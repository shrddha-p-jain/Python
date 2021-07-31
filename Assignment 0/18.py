def vow_c(str1):
    count=0
    vow="aeiouAEIOU"
    for char in str1:
        if char in vow:
            count=count+1
    return count
str2=input("enter string: ")
print(vow_c(str2))
            
