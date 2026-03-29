class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #s1 = "abc", s2 = "lecabee"

        #brute force solution:
        #hashmap of frequency counts of  s1 
        # traverse s2 and once we see a char from hash then start expanding the window 

        if len(s1)>len(s2):
            return False 

        # count1={}
        # for i in range(len(s1)):
        #     count1[s1[i]]=count1.get(s1[i],0)+1

        # for i in range(len(s2)):
        #     count=count1.copy()
        #     for j in range(i,len(s2)):
        #         if s2[j] not in count:
        #             break 
        #         count[s2[j]]-=1

        #         if count[s2[j]]==0:
        #             del count[s2[j]]
                
        #         if not count:
        #             return True 
        # return False 

               
        #optimized approach : sliding window algorithm 
        # what is my window : len(s1)
        # what state am I keeping: Yes_permute=T/F 
        # what is right ? => expore the string 
        # what is left? => fixed start of the "permuted" string => moves if the window is invalid 
        # when is the winodw invalid ? => right-left+1>len(s1)

        
        count1={}
        for i in range(len(s1)):
            count1[s1[i]]=count1.get(s1[i],0)+1
        
        count2={}
        left=0
        for right in range(len(s2)):
            count2[s2[right]]=count2.get(s2[right],0)+1
            if right-left+1>len(s1):
                count2[s2[left]]-=1
                if count2[s2[left]]==0:
                    del count2[s2[left]]
                left+=1
            if count1==count2:
                return True 
        return False 



            
            







        