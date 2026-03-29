class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        #s = "zxyzxyz" length=3 
        # brute force : traverse the string + count characters 
        #use a set for unique characters 
        #update length accordingly 




       # in this brute force solution O(n2) 
       # i= the start of each new 
       # j= explores the longuest substring 

        max_length=0
        for i in range(len(s)):
            #initialize set at every start of the string 
            seen=set()
            for j in range(i,len(s)): #start at i and not i+1 so we dont miss the single characters substrings
                if s[j] in seen:
                    break 
                seen.add(s[j])
                max_length=max(max_length,j-i+1)
        return max_length


                    