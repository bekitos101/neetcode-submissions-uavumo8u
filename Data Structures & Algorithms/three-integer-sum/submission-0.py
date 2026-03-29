class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #brute force solution :check for every triplet in the array 
        #nums = [-1,0,1,2,-1,-4] n=6
        #i=0 j=1 k=2 => nums[i]+nums[j]+nums[k]=0 => [-1,0,1]
        #i=0 j=1 k=3 => nums[0]+nums[1]+nums[3]=1=> skip
        #i=0 j=1 k=4 => nums[0]+nums[1]+nums[4]=0 => [1,0,-1] =>appended although we should skip it
        # solution: sort the numbers before adding them to the set

        ans=set() 
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i]+nums[j]+nums[k]==0:
                        ans.add(tuple(sorted ([nums[i],nums[j],nums[k]])))
        return [list(s) for s in ans]

        