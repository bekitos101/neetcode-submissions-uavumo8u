class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Brute force solution - python optimal  
        # initially we wanted to append to a string but strings are expensive in python 
        #appending to a string makes you create a new string each time and append to it 
        #this implementation is O(n2) therefore we use the implementation of the list
        clean_string=[]
        for c in s:
            if c.isalnum():
                clean_string.append(c.lower())
        clean_string_joined="".join(clean_string)
        return clean_string_joined[::-1]==clean_string_joined