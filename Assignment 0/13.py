s = input("enter a string: ")
y = int(input("Position where you want to delete:"))
if(y<0):
    print("Position must be positive")
else:
    output = ''
    for i in range(len(s)):
        if(i!=y-1):
            output+=s[i]
    print(output)
