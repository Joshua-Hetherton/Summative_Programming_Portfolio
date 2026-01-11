"""Searching algorithm 
returns the largest, smallest, mode, median, 1st IQF & 3rd IQF of an array.
User should be able to enter an array of their choice.
"""

def find_largest(given_array):
    """
    Given an array, it returns the largest value in the array given

    Args:
        given_array (List[int]): The array that was given by the user

    Returns:
        largest_value (int): The largest value in the array
    """
    largest_value=None
    for value in given_array:
        
        if value>largest_value:
            largest_value=value

    return largest_value


def find_smallest(given_array):
    """
    Given an array, it returns the smallest value in the array given

    Args:
        given_array (List[int]): The array that was given by the user

    Returns:
        smallests_value (int): The smallest value in the array
    """
    smallest_value=None
    for value in given_array:
        
        if value < smallest_value:
            smallest_value=value

    return smallest_value

def find_median():
    """
    Docstring for find_median
    """
    pass

def find_mode():
    """
    Docstring for find_mode
    """
    pass

def find_interquartial_range():
    """
    Docstring for find_interquartial_range
    """
    pass

def is_array_valid():
    """
    Docstring for is_array_valid
    """
    pass

def calculate_statistics():
    """
    Docstring for calculate_statistics
    """
    pass