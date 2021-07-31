def mult_table(n):
    for i in range(1,11):
        print("{0} * {1} = {2}".format(i,n, n*i))
    

def mult_table_range(x,y):
    for i in range(x,y+1):
        mult_table(i)
        print("\n")

mult_table_range(11,13)
    
