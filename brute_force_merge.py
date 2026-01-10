def combine_arrays(left_array, right_array):
    """
    Rejoins the branches of the array, now in a sorted order.
    
    left_array (List[int]): The left branch of the array
    right_array (List[int]): The right branch of the aray
    """
    output=[]
    left_index=0
    right_index=0
    try:
        while (left_index< len(left_array) and right_index < len(right_array)): 
            if left_array[left_index] <= right_array[right_index]:
                output.append(left_array[left_index])
                left_index +=1
            elif right_array[right_index] <= left_array[left_index]:
                output.append(right_array[right_index])
                right_index +=1
        #Checks for any remaining elements not sorted, by appending any of the remaining elements onto the output
        output.extend(left_array[left_index:]+ right_array[right_index:])
    except IndexError:
        print("Index Error occured when doing merging of the merge sort")
    return output
            


def merge_sort(given_array):
    """
    Docstring for merge_sort
    
    :param list_to_sort: Description
    """
    if len(given_array)<=1:
        return given_array
    middle = len(given_array)//2 #Splits the array in half

    left_array= given_array.slice(0, middle)
    right_array= given_array.slice(middle, len(given_array))


    #Recursively splits the arrays into halves until the length is 1
    recursive_left = merge_sort(left_array)
    recursive_right = merge_sort(right_array)

    return combine_arrays(recursive_left, recursive_right)

    
    

