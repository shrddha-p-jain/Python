
def skip_given(start,end,skip):
    if start>end:
        print("Invalid range")
    else:
        for i in range(start,end+1):
            if str(i) in skip:
                continue
            print(i,end="  ")



start = int(input("Enter the starting number: "))
end = int(input("Enter the end number: "))
skip = input("Enter the numbers you want to skip, separated by space: ").split(" ")

skip_given(start,end,skip)
