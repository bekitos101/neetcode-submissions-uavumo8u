class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Brute force 
        #s = "zxyzxyz" "" set=() max=3

        # max_length=0
        # for i in range(len(s)):
        #     seen=set()
        #     length=0
        #     for j in range(i,len(s)):
        #         if s[j] in seen:
        #             max_length=max(max_length,length)
        #             break
        #         seen.add(s[j])
        #         length+=1
        # return max_length

        #sliding window solution 

        """
        
        s="pwwwwwwwwwkew"
        left=0 right=0 seen={p} right=1
        left=0 right=1 seen={pw} right=2
        left=0 right=2 s[right] in seen  seen={ww}
        
        
        """
        left=0
        right=0 
        window_seen=set()
        max_length=0
        while right<len(s):
            while s[right] in window_seen:
                window_seen.remove(s[left])
                left+=1

            window_seen.add(s[right])
            max_length=max(max_length,right-left+1)
            right+=1
        return max_length




                

                
            





