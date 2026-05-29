# Recursively calculate the sum of all elements of the given list
 
def arrayTotalSum(a):
 
    # Calculating length of array
    length = len(a)
 
    # If array length is 1 just return the element
    if length == 1:
        return a[0]
 
    # return current element and received sum 
    return a[0] + arrayTotalSum(a[1:])
 
a = [1,2,3,6]
 
# Displaying result
print("Array total sum: ",arrayTotalSum(a))
