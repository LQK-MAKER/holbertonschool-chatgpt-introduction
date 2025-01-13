#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer using recursion.

    Parameters:
        n (int): The number for which the factorial is to be calculated. 
                 Must be a non-negative integer.

    Returns:
        int: The factorial of the input number. If n is 0, returns 1 (as 0! = 1).
    """
    if n == 0:
        return 1  # Base case: factorial of 0 is 1
    else:
        return n * factorial(n - 1)  # Recursive call

# Get the input number from the command-line arguments
f = factorial(int(sys.argv[1]))  # Convert the first argument to an integer
print(f)  # Print the factorial of the input number
