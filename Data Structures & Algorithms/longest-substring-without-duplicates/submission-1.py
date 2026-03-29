class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        #s = "zxyzxyz" length=3 
        # brute force : traverse the string + count characters 
        #use a set for unique characters 
        #update length accordingly 




       # in this brute force solution O(n2) time complexity O(n) space complexity 
       # i= the start of each new 
       # j= explores the longuest substring 
       # the length of the substring is j-i+1 (accounting for the 0 index )

        # max_length=0
        # for i in range(len(s)):
        #     #initialize set at every start of the string 
        #     seen=set()
        #     for j in range(i,len(s)): #start at i and not i+1 so we dont miss the single characters substrings
        #         if s[j] in seen:
        #             break 
        #         seen.add(s[j])
        #         max_length=max(max_length,j-i+1)
        # return max_length


        #Optimized approach same idea but we optimize it
        # two pointers
        #left= start of each new substring 
        #right=explores the substring 
        # s = "zxyzxyz" 

        #sliding window : core algrithm 
        # left = 0
        # for right in range(len(arr)):   # expand
        #     add(arr[right])            
        #     while window_is_invalid():  # shrink
        #         remove(arr[left])
        #         left += 1


        left=0
        seen=set()
        max_length=0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1 
            
            seen.add(s[right])   
            max_length=max(max_length,right-left+1)
        return max_length
  