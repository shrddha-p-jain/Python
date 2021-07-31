s = input("enter a string: ")
s_split = s.split()
s_odd_words = []

for i in s_split:
    if len(i)%2!=0:
        s_odd_words.append(i)

print("The words with odd number of letters are: ",s_odd_words)
