# Program to recursively check if a given array is sorted or not
 
 
def checkSorted(a):
 
    # Calculating length of array
    length = len(a)
 
    # If array length is 0,1 means we need not to check further
    if length == 1 or length == 0:
        return True
 
    # return true if both below conditions are true
    return a[0] <= a[1] and checkSorted(a[1:])
 
 
a = [1,2,3,5,6,8,2]
 
# Displaying result
if checkSorted(a):
    print("\nYes given array is sorted")
else:
    print("\nNo given array is not sorted")
