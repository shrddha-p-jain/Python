s = input("Enter a string: ")
l = int(input("Enter length:"))
s_words = s.split()
if l <=0:
    print("Invalid length")
else:
    flag=0
    for i in s_words:
        if len(i)>l:
            flag=1
            print(i, end = " ")
    if flag==0:
        print("None")
        
