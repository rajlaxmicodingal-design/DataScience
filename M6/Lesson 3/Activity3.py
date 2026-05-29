# Recursively find the largest number in the array
 
def MaxElementArray(a):
 
    # Calculating length of array
    length = len(a)
 
    # If array length is 1 just return the element
    if length == 1:
        return a[0]
 
    # Return the largest number among current largest and current element
    return max(a[0],MaxElementArray(a[1:]))
 
a = [1,2,234,234,745,3,6,653]
 
# Displaying result
print("Largest element of array: ",MaxElementArray(a))
