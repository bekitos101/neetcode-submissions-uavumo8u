class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #brute force solution 
        #Time complexity :o(nlog(n)) for sorting + o(n) for comparison => overall o(nlog(n))
        #Space complexity: o(n) for python space complexity 
        return sorted(s)==sorted(t)
        
        # Optimized solution:
        # Goal: reduce time complexity to O(n)
        # Count the frequency of each character in both strings.
        # If the frequency maps are identical, the strings are anagrams.
        # No sorting is needed because dictionary equality ignores order.
        
        freq_s={}
        for char in s:
            freq_s[char]=freq_s.get(char,0)+ 1
        freq_t={}
        for char in t: 
            freq_t[char]+=freq_t.get(char,0)+1

        return freq_s==freq_t 

        