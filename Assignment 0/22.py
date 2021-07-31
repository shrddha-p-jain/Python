def num_div(start,end):
    for i in range(start,end+1):
        if(i%2==0 or i%7==0):
            print(i,end="  ")

num_div(1,200)
