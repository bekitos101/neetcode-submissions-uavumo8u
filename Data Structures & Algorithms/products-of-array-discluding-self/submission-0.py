class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #brute force solution

        ans=[1]*len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j:
                    ans[i]*=nums[j]

        return ans