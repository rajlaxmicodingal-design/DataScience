# Program to find factorial of any number using recursion 
def fac(n):
    # When n is 1 or 0, return 1 
    if(n==1 or n==0):
        return 1
    # Factorial of n = n*n-1*n-2...1
    return n*fac(n-1)
n = int(input("Enter your number : "))
print ("Factorial of", n, "is : ",fac(n))
