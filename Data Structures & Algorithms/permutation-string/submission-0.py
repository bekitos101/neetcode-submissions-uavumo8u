class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #s1 = "abc", s2 = "lecabee"

        #brute force solution:
        #hashmap of frequency counts of  s1 
        # traverse s2 and once we see a char from hash then start expanding the window 

        if len(s1)>len(s2):
            return False 

        count1={}
        for i in range(len(s1)):
            count1[s1[i]]=count1.get(s1[i],0)+1

        for i in range(len(s2)):
            count=count1.copy()
            for j in range(i,len(s2)):
                if s2[j] not in count:
                    break 
                count[s2[j]]-=1

                if count[s2[j]]==0:
                    del count[s2[j]]
                
                if not count:
                    return True 
        return False 

                







        