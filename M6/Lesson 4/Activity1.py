# Program to reverse a number using recursion 
 
def reverseNumber(num):
    if(num > 0):
        # if the input number is not 0 then get the last digit and add to the current reversesd number received
        last = num%10
        if(num//10>0):
            current_number = reverseNumber((int)(num // 10))
            return last*pow(10,len(str(current_number))) + current_number
        return num
 
n = int(input("Enter your number : "))
print("Reversed : ",reverseNumber(n))
