class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #temperatures = [30,38,30,36,35,40,28]

        #brute force approach 
        #we fix each temperatue => for each fixed temperature, we calculate the number of temperatures after until it gets warm again 
        #once we find it then we break and move to the next temperature 

        ans=len(temperatures)*[0]
        for i in range(len(temperatures)):
            for j in range(i+1,len(temperatures)):
                if temperatures[j]>temperatures[i]:
                    ans[i]=j-i
                    break
        
        return ans 
        




        