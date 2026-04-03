class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #temperatures = [30,38,30,36,35,40,28]

        #brute force approach 
        #we fix each temperatue => for each fixed temperature, we calculate the number of temperatures after until it gets warm again 
        #once we find it then we break and move to the next temperature 

        # ans=len(temperatures)*[0]
        # for i in range(len(temperatures)):
        #     for j in range(i+1,len(temperatures)):
        #         if temperatures[j]>temperatures[i]:
        #             ans[i]=j-i
        #             break
        
        # return ans 
        
        #optimized solution
        # there is a lot of redundency when it comes to recomputing temperatures 
        # temperatures = [38,30,36,35,40] => answer= [4,1,2,1,0]
        # In the case where we have a series of temperatures like this one, we want to check each time if we cam maybe 
        # resolve the current temperature we are indexing + some of the temperatures before it
        # this is useful when we have a series of decreasing temperatures like this one 38,36,35,40 
        # so the temp=40 resolves the temp 35, and temp 36, and temp 38 at the same time 
        # we need a data structure that stores these decreasing temperatures and helps us resolve them 
        #from the last one onwards => monotonic stack 


        #algorithm 
        stk=[]
        ans=[0]*len(temperatures)
        for i,temp in enumerate(temperatures):
            while stk and  temp>temperatures[stk[-1]]:
                idx=stk.pop()
                ans[idx]=i-idx 
            stk.append(i)
        return ans 

        #dry run 
        #temperatures = [30,38,30,36,35,40,28]
        #i=0 temperatures[0]=30 stk=[] => stk=[0]
        #i=1 temperatures[1]>temperatures[0] => stk=[] , idx=0 ans[0]=1-0=1 
 

            






        