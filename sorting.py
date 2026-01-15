"""Selection & Bubble sort. 
User should be able to enter an array of their choice. 
User should be able to specify Ascending/Descending, default sort if not specified should be Ascending.
"""

def bubble_sort(given_array,Ascending=True):
    array_length= len(given_array)

    for i in range(array_length):
        for j in range(0, array_length-i-1):
            if Ascending:
                if given_array[j] > given_array[j+1]:
                    given_array[i], given_array[j+1]=given_array[j+1],given_array[i]
                
            else:
               if given_array[j] < given_array[j+1]:
                    given_array[i], given_array[j+1]=given_array[j+1],given_array[i] 
    
    

    return given_array

def selection_sort(given_array,Ascending=True):

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

        
