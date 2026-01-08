"""Factorial calculation using recursion.
You should calculate the factorial of a given number by a user.

This implementation uses recursion to calculate the factorial
"""

def calculate_factorial(user_input):
    """
    Calculates the factorial of a given number using recursion.
    
    Args:
        user_input (int): The number for which to calculate the factorial

    Returns:
        int: The factorial of the given number
    """
    if user_input==0 or user_input==1:
        return 1
    
    else:
        return calculate_factorial(user_input-1) * user_input