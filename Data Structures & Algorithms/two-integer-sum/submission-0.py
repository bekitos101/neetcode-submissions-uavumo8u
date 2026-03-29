class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force solution 
        #nums = [3,4,5,6], target = 7
        # check each pair of the array 
        ans=[]
        for i,num in enumerate(nums):
            rest=target-num 
            for j in range(i+1,len(nums)):
                if nums[j]==rest:
                    ans.append(i)
                    ans.append(j)
        return ans  


        
