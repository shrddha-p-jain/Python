s = input("Enter a String: ")
def change(s):
    s_change = ''
    for i in s:
        if i==',':
            s_change +='.'
        elif i=='.':
            s_change += ','
        else:
            s_change += i
    return s_change

print(change(s))
    
        
