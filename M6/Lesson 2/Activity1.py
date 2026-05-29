def headrec(n, num):
    # Base case: if n exceeds num, terminate the recursion
    if n > num:
        return
    # Recursive call with the next value
    headrec(n + 1, num)
    # Print the current value of n after returning from the recursive call
    print(n)

# Prompt the user to enter the value of n
n = int(input("Enter n to print 1 to n: "))

# Initial call to the headrec function starting from 1
headrec(1, n)
