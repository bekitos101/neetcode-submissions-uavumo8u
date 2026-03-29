class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #O(nlogn + mlogm)
        # return sorted(s) == sorted(t)
        
        #optimized solution 
        
        # frequency_s={}
        # for char in s:
        #     frequency_s[char]=frequency_s.get(char,0)+1        
        
        # frequency_t={}
        # for char in t:
        #     frequency_t[char]=frequency_t.get(char,0)+1        
        
        # return frequency_t==frequency_s

        #even more optimized solution 

        if len(s) != len(t):
            return False
        
        hash_map={}

        for char in s: 
            hash_map[char]=hash_map.get(char,0)+1
        
        for char in t:
            if char not in hash_map:
                return False 
            hash_map[char]-=1
            if hash_map[char]<0:
                return False 
        return True 