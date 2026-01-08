

def palindrome_substrings_count(input_str):
    """
    Counts all the Palindrome substrings in a given input string, using memorisation.
    
    Args:
        input_str (str): The input string in which to count palindrome

    Returns:
        int: The count of palindrome substrings in the input string

    """
    counter=0
    len_str = len(input_str)
    memory={}

    ##Checks if a substring is a palindrome
    def is_palindrome(start,end):
        """Checks if a Substring is a palindrome
        start, end: denotes the start and end of substring
        """
        #Checks if it is already in memory
        if(start,end) in memory:
            return memory[(start,end)]
        
        #Checks if there's only one character
        if start==end:
            return True
        
        #Checks if only two characters are there, and if they are the same
        if start+1==end:
            return input_str[start]==input_str[end]
        

    #Checks for all possible substrings
    for i in range(len_str):
         for j in range(i, len_str):
                if(i,j) not in memory:
                   memory[(i,j)] = is_palindrome(i,j)
                if memory[(i,j)]:
                    counter+=1
    return counter
                