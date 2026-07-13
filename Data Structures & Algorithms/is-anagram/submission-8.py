class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #brute force solution 
        #Time complexity :o(nlog(n)) for sorting + o(n) for comparison => overall o(nlog(n))
        #Space complexity: o(n) for python space complexity 
        # return sorted(s)==sorted(t)
        
        # Optimized solution:
        # Goal: reduce time complexity to O(n)
        # Count the frequency of each character in both strings.
        # If the frequency maps are identical, the strings are anagrams.
        # No sorting is needed because dictionary equality ignores order.
        # time complexity: O(n) space complexity: o(1)
        # freq_s={}
        # for char in s:
        #     freq_s[char]=freq_s.get(char,0)+ 1
        # freq_t={}
        # for char in t: 
        #     freq_t[char]=freq_t.get(char,0)+1

        # return freq_s==freq_t 


        #We want an even cleaner solution : single pass - single hashmap
        # we track the difference in frequencies between the two strings: 
        # if we track char in s, the frequency is +1 if we track it in t the frequency is -1 
        # if the strings are anagarms every increment is cancelled by every decrement which means 
        # the final values of the hashmap will be 0. 

        if len(s)!=len(t):
            return False 
        
        count={}
        for char in s:
            count[char]=count.get(char,0)+1
        for char in t:
            count[char]=count.get(char,0)-1

        return all(value==0 for value in count.values())            

        