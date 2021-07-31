print("S")
for i in range(5):
    for j in range(7):
      #  if(i==0 or i==2 or i==4):
       #     print("*", end="")
        if(i==1):
            if(j==0):
                print("*",end="")
         #   else:
         #       print(" ",end="")
        elif(i==3):
            if(j==6):
                print("*",end="")
            else:
                print(" ",end="")
        else:
            print("*", end="")
    print(" ")

print("")
print("F")
for i in range(5):
    for j in range(7):
        if(i==0):
            print("*",end = "")
        if(i==2):
            if(j<4):
                print("*",end="")
        else:
            if(j==0):
                print("*",end = "")
    print("")
        


