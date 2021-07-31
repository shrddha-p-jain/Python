inp = tuple(input("Enter the numbers separated by space: ").split())
odd = 0
even = 0
for i in inp:
    if int(i)%2==0:
        even+=1
    else:
        odd+=1
print("There are {} odd numbers and {} even numbers in the tuple".format(odd, even))
