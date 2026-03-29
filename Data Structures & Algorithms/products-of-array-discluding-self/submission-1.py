class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #brute force solution

        ans=[-1]*len(nums)
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i!=j:
        #             ans[i]*=nums[j]

        # return ans

        #optimized solution : using prefix and suffix sum 

        prefix=1
        #nums=[1,2,4,6]
        #prefix=[1,1,2,8]

        for i in range(len(nums)):
            ans[i]=prefix
            prefix*=nums[i]
        
        suffix=1
        for i in range(len(nums)-1,-1,-1):
            ans[i]*=suffix
            suffix*=nums[i]
        return ans 
