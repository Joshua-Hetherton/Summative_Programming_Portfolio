"""Searching algorithm 
returns the largest, smallest, mode, median, 1st IQF & 3rd IQF of an array.
User should be able to enter an array of their choice.
"""
import sorting
def find_largest(given_array):
    """
    Given an array, it returns the largest value in the array given

    Args:
        given_array (List[int]): The array that was given by the user

    Returns:
        largest_value (int): The largest value in the array
    """
    largest_value=given_array[0]
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
    smallest_value=given_array[0]
    for value in given_array:
        
        if value < smallest_value:
            smallest_value=value

    return smallest_value

def find_median(given_array):
    """
    FInds the median of the array.
    If there is no true middle, the 2 middle values will be averaged, otherwise, it returns the middle.
    In this case, the array is sorted using
    Args:
        given_array (List[int]): The array that was given by the user
    
    Returns:
        median_value (int): The median value of the array
    """
    
    sorted_array=sorting.bubble_sort(given_array, Ascending=True)
    array_length=len(sorted_array)

    if array_length==0:
        return None

    #Checks the length of the array. If it is an even number, it averages the 2 middle values
    if array_length % 2 ==0:
        middle_1=sorted_array[array_length//2 - 1]
        middle_2=sorted_array[array_length// 2]
        median_value=(middle_1+middle_2)/2
        return median_value

    else:
        return sorted_array[array_length//2]

def find_mode(given_array):
    """
    Finds the mode of the given array.
    The mode is the value that appears most often in the array.
    A dictionary is used to keep track of the counts of each value that is found in the array

    Args:
        given_array (List[int]): The array given by the user

    Returns:
        find_max_frequency (int): The mode of the array
    """
    if len(given_array)==0:
        return None
    
    frequency_dict={}
    for value in given_array:
        if value not in frequency_dict:
            #If a new value is found, it is added to the dict with a count of 1
            frequency_dict[value]=1
        else:
            frequency_dict[value]+=1
    #Finding the value with the highest frequency
    find_max_frequency=0
    for i in frequency_dict:
        if i > find_max_frequency:
            find_max_frequency=i


    return find_max_frequency


def find_interquartial_range(given_array):
    """
    Finds the first and third interquartial range of the given array
    Args:
        given_array (List[int]): The array given by the user
    Returns:

    """
    #Checks if the array is empty, as if it is empty, the IQR cant be found
    if len(given_array)==0:
        return None, None
    
    sorted_array=sorting.bubble_sort(given_array,Ascending=True)
    array_length=len(sorted_array)

    if array_length % 2 ==0:
        lower_half=sorted_array[:array_length//2]
        upper_half=sorted_array[array_length//2:]
    else:
        lower_half=sorted_array[:array_length//2]
        upper_half=sorted_array[array_length//2+1:]

    first_Quart=find_median(lower_half)
    third_Quart=find_median(upper_half)

    return first_Quart, third_Quart

def is_array_valid(given_array):
    """
    Checks if the array the user has provided is valid
    """
    #Checks if any element isnt an integer
    if not all(isinstance(x, int) for x in given_array):
        return False
    #Checks given_array type
    if not isinstance(given_array, list):
        return False
    
    if len(given_array)==0:
        return False
    #Passes validation
    return True


def calculate_statistics(given_array):
    """
    Uses all the functions in search.py to calculate the statistics of a given array.
    Args:
        given_array (List[int]): The array given by the user
    Returns:
        statistics_list (List): A list containing the smallest, largest, mode, median, 1st IQF & 3rd IQF of the array
    """
    statistics_list=[]

    #Checking if array is valid
    if not is_array_valid(given_array):
        return None
    
    smallest=find_smallest(given_array)
    largest=find_largest(given_array)
    mode=find_mode(given_array)
    median=find_median(given_array)
    first_QR, third_QR=find_interquartial_range(given_array)

    statistics_list.append(smallest, largest, mode, median, first_QR, third_QR)

    return statistics_list