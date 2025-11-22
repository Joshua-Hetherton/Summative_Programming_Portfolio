"""Palindrome Substrings counter using memoization.
You should allow the user to input the initial string.
"""

def palindrome_substrings_count(str):
    counter=0
    len_str = len(str)
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
            return str[start]==str[end]
        #
        

    #Checks for all possible substrings
    for i in range(len_str):
         for j in range(i, len_str):
                if(i,j) not in memory:
                   memory[(i,j)] = is_palindrome(i,j)
                if memory[(i,j)]:
                    counter+=1
    return counter
                