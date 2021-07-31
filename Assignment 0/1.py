n1 = int(input("Enter number:"))
def factorial(n):
    fact = 1
    if n<0:
        return("Not Defined (Negative Input)")
    else:
        for i in range(2, n+1):
            fact = fact*i
    return fact

print("factorial of {} is {}".format(n1,factorial(n1)))

