# Program to send if the number is power of 4 or not
 
# Take input
n = int(input("Enter your number : "))
 
def checkIfPower(n):
    # if n is less than equal to 0 just say no
    if(n<=0):
        return False
    # if we reach lowest power of n just retur true
    if(n==1):
        return True
    if(n%4==0):
        return checkIfPower(n/4)
    return False
 
if(checkIfPower(n)):
    print("Power of 4")
else:
    print("Not power of 4")
