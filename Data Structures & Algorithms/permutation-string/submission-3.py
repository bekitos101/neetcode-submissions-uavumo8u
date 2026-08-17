class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #brute force approach 
        #s1={a:1,b:1,c:1}
        #generate every substring of s2 with length len(s1)
        #count characters in that substring
        #compare its frequency map with s1 
        #if valid, the permutation exists

        # count_s1={}
        # for char in s1:
        #     count_s1[char]=count_s1.get(char,0)+1

        # for i in range(len(s2) - len(s1) + 1):
        #     substring_count={}
        #     for j in range(i,i+len(s1)):
        #         substring_count[s2[j]]=substring_count.get(s2[j],0)+1

        #     if substring_count==count_s1:
        #         return True 
        
        # return False

        #sliding window approach
        #explore every len(s1) substring 
        #expand window: add new character to substring 
        #shrink window condition:  window=len(s1)
        #window is valid : count_s1==count_substring
        
        count_s1={}
        for char in s1:
            count_s1[char]=count_s1.get(char,0)+1
        left=0
        count_substring={}

        for right in range(len(s2)):
            #expand window 
            count_substring[s2[right]]=count_substring.get(s2[right],0)+1
            
            #once window valid
            if right-left+1==len(s1):
                #check valid condition 
                if count_s1==count_substring:
                    return True     

                #slide window if non valid condition 
                count_substring[s2[left]]-=1
                if count_substring[s2[left]]==0:
                    count_substring.pop(s2[left])

                left+=1
                
        return False             




        

        


        