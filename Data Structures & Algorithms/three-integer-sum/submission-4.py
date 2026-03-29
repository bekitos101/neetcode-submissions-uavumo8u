class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #brute force solution :check for every triplet in the array 
        #nums = [-1,0,1,2,-1,-4] n=6
        #i=0 j=1 k=2 => nums[i]+nums[j]+nums[k]=0 => [-1,0,1]
        #i=0 j=1 k=3 => nums[0]+nums[1]+nums[3]=1=> skip
        #i=0 j=1 k=4 => nums[0]+nums[1]+nums[4]=0 => [1,0,-1] =>appended although we should skip it
        # solution: sort the numbers before adding them to the set this ensures we dont
        # have [-1,0,1] and [1,0,-1] both in ans 
        
        # ans=set() 
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         for k in range(j+1,len(nums)):
        #             if nums[i]+nums[j]+nums[k]==0:
        #                 ans.add(tuple(sorted ([nums[i],nums[j],nums[k]])))
        # return [list(s) for s in ans]

        #optimized approach 
        #nums = [-1,0,1,2,-1,-4] n=6
        #sorted_nums=[-4,-1,-1,0,1,2] n=6 
        # i=0 num=-4 
        
        ans_set=set()
        nums.sort()
        for i, num in enumerate(nums):
            complement=-num
            left=i+1
            right=len(nums)-1
            while left<right:
                if nums[left]+nums[right]==complement:
                    ans_set.add(tuple([nums[i],nums[left],nums[right]]))
                    left+=1
                    right-=1
                elif nums[left]+nums[right]<complement:
                    left+=1
                else:
                    right-=1
        return [list(s) for s in ans_set]
    

        