n = input('Enter a number between 200 and 220: ')
if(int(n)<200 or int(n) > 220):
    print("Invalid number")
else:
    odd_digits = []
    for i in n:
       # print (i)
        if(int(i)%2!=0):
            odd_digits.append(i)
    if not odd_digits:
        print("No odd digits")
    else:
        odd_digits = ",".join(odd_digits)
        print(odd_digits)        

        
        


'''    
    output = ''
    for i in n:
        if(int(i)%2==1):
            if(output == ''):
                output+= i
            else:
                output = output + ',' + i
print(output)
'''
