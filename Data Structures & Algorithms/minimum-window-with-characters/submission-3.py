class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #s = "OUZODYXAZV", Required
        # i=0 "O"
        #      j=0 "O"  "XYZ"
        #      j=1  "OU" "XYZ"
        #      j=2  "OUZ"   "XY"
        #      j=4   "OUZO" "XY"
        #     j=5   "OUZOD" "XY"
        #     j=6   "OUZODY" "X" 
        #     j=7   "OUZODYX" "" => l=7 min =7 

        #i=1 
        #Repeat

        #s = "OUZODYXAZV", t = "XYZ"
        #Brute force solution : O(n2) time O(n) space 

        # def get_count(t):
        #     count_t = {}
        #     for char in t:
        #         count_t[char] = count_t.get(char, 0) + 1
        #     return count_t

        # count_t={}
        # min_length=float("inf")
        # joined_substring=""
        # for i in range(len(s)):
        #     substring=[]
        #     count_t=get_count(t)
        #     for j in range(i,len(s)):
        #         substring.append(s[j])
        #         if s[j] in count_t:
        #             count_t[s[j]]-=1
        #             if count_t[s[j]]==0:
        #                 count_t.pop(s[j])
        #         if not count_t:
        #             if j-i+1<min_length:
        #                 min_length=j-i+1
        #                 joined_substring="".join(substring)
        #                 break

        # return joined_substring

        #sliding window approach optimization 

        def get_count(t):
            count_t = {}
            for char in t:
                count_t[char] = count_t.get(char, 0) + 1
            return count_t

        
        min_length=float("inf")
        left=0
        window_count={} #keep the count of chars in current window
        count_t=get_count(t) #the count of characters in t 
        required=get_count(t) # the mandatory characters in every window (readonly)
        substring=""
        min_substring=""
        length=0
        for right in range(len(s)):
            #expand window actions:
            #update count in current window 
            #process t existance in current window
            #update length 
            window_count[s[right]]=window_count.get(s[right],0)+1
            if s[right] in count_t:
                count_t[s[right]]-=1
                if count_t[s[right]]==0:
                    count_t.pop(s[right])
            length=right-left+1
            #Minimum window -> shrink when window is valid 
            #Can we further shrink the window and stay valid? 
            #valid window -> count_t is empty -> shrink while valid

            while not count_t:
                #current window is valid : record it 
                length=right-left+1
                substring=s[left:right+1]
                if length<min_length:
                    min_length=length
                    min_substring=substring
                #shrink window further 
                window_count[s[left]]-=1

                #did removing make it invalid ?
                if s[left] in required:
                    if window_count[s[left]]<required[s[left]]:
                        count_t[s[left]]=count_t.get(s[left],0)+1
               
            
                left+=1

        return min_substring





                










        