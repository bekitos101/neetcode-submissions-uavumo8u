class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Brute force solution - python optimal  
        # initially we wanted to append to a string but strings are expensive in python 
        #appending to a string makes you create a new string each time and append to it 
        #this implementation is O(n2) therefore we use the implementation of the list
        #Time complexity O(n) Space complexity O(n)
        # clean_string=[]
        # for c in s:
        #     if c.isalnum():
        #         clean_string.append(c.lower())
        # clean_string_joined="".join(clean_string)
        # return clean_string_joined[::-1]==clean_string_joined

        #can we make the space complexity o(1)

        start=0
        end=len(s)-1

        while start<=end:

            if not s[start].isalnum():
                start+=1
            elif not s[end].isalnum():
                end-=1
            elif s[start].lower()!=s[end].lower():
                return False
            else:
                start+=1
                end-=1
        return True  
