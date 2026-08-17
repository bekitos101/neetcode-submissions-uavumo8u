class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #brute force approach 
        #s1={a:1,b:1,c:1}
        #generate every substring of s2 with length len(s1)
        #count characters in that substring
        #compare its frequency map with s1 
        #if valid, the permutation exists

        count_s1={}
        for char in s1:
            count_s1[char]=count_s1.get(char,0)+1
        
        #the last substring will start at the index len(s2) - len(s1)
        #this makes sure we always have enough len(s1) characters there 
        for i in range(len(s2) - len(s1) + 1):
            substring_count={}
            for j in range(i,i+len(s1)):
                substring_count[s2[j]]=substring_count.get(s2[j],0)+1

            if substring_count==count_s1:
                return True 
        
        return False



        

        


        