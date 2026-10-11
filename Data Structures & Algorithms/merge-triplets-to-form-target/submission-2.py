class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        # def merge(l,m,n):
        #     res=[]
        #     for a,b in zip(l,m):
        #         number=max(a,b)
        #         res.append(number)
        #     return res==n
        def merge_2(l,m):
            res=[]
            for a,b in zip(l,m):
                res.append(max(a,b))
            return res 
        def check(triplet,target):
            for i in range(len(triplet)):
                if triplet[i]>target[i]:
                    return True 
            return False

        res=[0,0,0]
        for i in range(len(triplets)):
            if check(triplets[i],target):
                continue
            # for j in range(i+1,len(triplets)):
            #     if check(triplets[j],target):
            #         continue
            #     if merge(triplets[i],triplets[j],target):
            #         return True

            res=merge_2(res,triplets[i])
            if res==target:
                return True 
     
        return False 


        