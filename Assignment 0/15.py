s = input("Enter a String: ")
def length(s):
    l = 0
    for i in s:
        l+=1
    return l
print("length of {} is {}".format(s,length(s)))
