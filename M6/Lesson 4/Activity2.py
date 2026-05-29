# Program to reverse a string using Recursion
 
def reverseString(s):
 
    # if only 1 char remains just return it
    if len(s) == 1:
        return s[0]
    
    firstchar = s[0]
    # get the already reversed string and add first char to end
    return reverseString(s[1:]) + firstchar
    
 
s = "Ankit Jadli"
print(reverseString(s))
