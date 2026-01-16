"""Dynamic Programming - Fibonacci Numbers.
Solve the Nth Fibonacci Numbers using dynamic programming. You should allow the user to input the number to find.
"""

def fibonacci(given_number):
    """
    Finds the nth Fibonacci of a given number using dynamic programming
    
    Args:
        given_number (int): The number to find the nth Fibonacci of, also known as (n)
    
    Returns:
        previous_values[1] (int): The nth Fibonacci number
    """
    if given_number <0:
        return -1
    if given_number==0:
        return 0
    if given_number==1:
        return 1
    
    previous_values=[0,1]
    for i in range(2, given_number+1):
        current_value= previous_values[0]+ previous_values[1]

        previous_values[0]= previous_values[1]
        previous_values[1]= current_value

    return previous_values[1]

