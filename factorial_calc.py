"""Factorial calculation using recursion.
You should calculate the factorial of a given number by a user.

This implementation uses recursion to calculate the factorial
"""

def calculate_factorial(user_input):
    if user_input==0 or user_input==1:
        return 1
    
    else:
        return f"{calculate_factorial(user_input-1) * user_input},"