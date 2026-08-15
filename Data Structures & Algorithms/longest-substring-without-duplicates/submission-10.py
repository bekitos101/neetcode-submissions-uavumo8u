class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #s = "zxyzxyz"
        #brute force solution 
        #we need to check each sequence of consecutively distinct characters
        #track unique characters using a set 
        #stop when a duplicate character is found 
        # max_seq=0
        # for i in range(len(s)):
        #     seen=set()
        #     for j in range(i,len(s)):
        #         if s[j] in seen:
        #             break
        #         seen.add(s[j])
        #         max_seq=max(max_seq,j-i+1)
        # return max_seq

        #optimized approach 
        left=0
        seen=set()
        max_seq=0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            max_seq=max(max_seq,right-left+1)
        return max_seq

        