def tailrec(n, num):
    # Base case: if n exceeds num, terminate the recursion
    if n > num:
        return
    # Print the current value of n
    print(n)
    # Recursive call with the next value (tail recursion)
    tailrec(n + 1, num)

# Prompt the user to enter the value of n
n = int(input("Enter n to print 1 to n: "))

# Initial call to the tailrec function starting from 1
tailrec(1, n)
