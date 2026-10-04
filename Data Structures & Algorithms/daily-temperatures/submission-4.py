class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Brute force Solution
        # fix each temperatures[i], then go through the next temperastures until 
        # we find a match, if we find a match break anfd continue 
        # TC : O(n2) SC:O(n)
        # res=len(temperatures)*[0]
        # for i in range(len(temperatures)):
        #     count=1
        #     for j in range(i+1,len(temperatures)):
        #         if temperatures[j]<=temperatures[i]:
        #             count+=1
        #         else:
        #             res[i]=count
        #             break
        # return res 

        """        
          temperatures=[30,38,30,36,35,40,28]
          i=0  j=1 temperastures[i]=30 temperastures[j]=38 res[0]=0+1=1  
          i=1  j=2 temperastures[i]=38 temperastures[j]=30 count=1 
               j=3 temperastures[i]=38 temperastures[j]=36 count=2 
               j=4 temperastures[i]=38 temperastures[j]=35 count=3 
               j=5 temperastures[i]=38 temperastures[j]=40 res[1]=3 
        """

        """
         #temperatures=[30,38,30,36,35,40,28]
         #30->push 
         #38->push 30-> pop 
         #36->push 30->pop
         #35->push
         #40-> 35pop , 36 pop,38 pop
         #28->psuh 
         #28->pop 
        
        
        """


        stk=[(temperatures[0],0)]
        res=len(temperatures)*[0]
        for i in range(1,len(temperatures)):
            while stk and temperatures[i]>stk[-1][0]: #[28,21,20,19,10,40]
                last_tem=stk[-1]
                res[last_tem[1]]=i-last_tem[1]
                stk.pop()
            stk.append((temperatures[i],i))
        return res


        #temperatures=[30,38,30,36,35,40,28]
        #[0,1,0,0,0,0,0]
        #stk((30,0))
        #i=1 temperastures[1]=38 last_tem=(30,0) 38>30 res[1]=1-0=1 stk=((38,1))
        #i=2 temperastures[2]=30 last_tem=(38,1) 30<38 stk=((38,1),(30,2))) 
        #i=3 temperastures[3]=36 last_tem=(30,2) 36>30 res[2]=3-2=1
        
                











        # """
        # res=[1,4,1,0,1,0,0]
        # temperatures = [30,38,30,28,35,40,28]
        # stk=(30) => temp that havent yet found a warmer day
        # i=1 temperatures[i]=38 30<38 res[0]=1 stk=(38:1)
        # i=2 temperatures[i]=30 30<38 stk=(38:1,30:2)
        # i=3 temperatures[i]=28 28<30  stk=(38:1,28:3)
        # i=4 temperastures[i]=35 35>28 res[4]=4-3=1 stk=(38:1)
        # i=5 temperastures[i]=40 40>38 res[1]=5-1=4 stk=()
        # i=6 temperastures[i]=28 stk=(28:6)    

        # """
        
                    













        