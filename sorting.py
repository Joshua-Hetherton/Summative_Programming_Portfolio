"""Selection & Bubble sort. 
User should be able to enter an array of their choice. 
User should be able to specify Ascending/Descending, default sort if not specified should be Ascending.
"""

def bubble_sort(given_array,Ascending=True):
    """
    The bubble sort function sorts the array using the bubble sort algorithm.
    It works by iterating through the array, comparing the adjacent elements and swapping them if they are in the wrong order.
    The process is repeated until the array is sorted.
    
    Args:
        given_array (List[int]): The array to be sorted
        Ascending (bool): If True, sort in ascending order, else descending order

    Returns:
        List[int]: The sorted array
    """
    array_length= len(given_array)

    for i in range(array_length):
        for j in range(0, array_length-i-1):
            if Ascending:
                if given_array[j] > given_array[j+1]:
                    given_array[j], given_array[j+1]=given_array[j+1],given_array[j]
                
            else:
               if given_array[j] < given_array[j+1]:
                    given_array[j], given_array[j+1]=given_array[j+1],given_array[j] 
    


    return given_array

def selection_sort(given_array,Ascending=True):
    """
    The selection sort function that sorts the array with the selection sort algorithm.
    It works by divding the array into a sorted and usorted list, and repeatedly selects the minimum and maximum element that is unsorted.
    This element is then swapped with the first unsorted element, and the process is repeated until sorted.
    
    Args:
        given_array (List[int]): The array to be sorted
        Ascending (bool): If True, sort in ascending order, else descending order
    Returns:
        List[int]: The sorted array
    """

    array_length= len(given_array)

    for i in range(array_length):
        #current_index is is element currently being compared
        current_index=i
        if Ascending:
            for j in range( i+1, array_length):
                if given_array[j] < given_array[current_index]:
                    current_index=j
        
        else:
            for j in range(i+1, array_length):
                if given_array[j] > given_array[current_index]:
                    current_index=j
        #Swapping the found max/min element with the first element
        given_array[i], given_array[current_index] = given_array[current_index], given_array[i]

    return given_array

        
