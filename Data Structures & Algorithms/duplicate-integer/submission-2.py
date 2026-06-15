class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        #Brute force solution 
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]==nums[j]:
        #             return True 
        # return False 
        
        
        
        seen=set()
        for num in nums:
            if num in seen:
                return True 
            seen.add(num)
        return False

        #Dry-run 
        # [1,2,3,3] num=1 seen=(1)
        # [1,2,3,3] num=2 seen=(1,2)
        # [1,2,3,3] num=3 seen=(1,2,3)
        # [1,2,3,3] num=3 seen=(1,2,3)
        # [1,2,3,3] num=3 seen=(1,2,3) => True 

      
        

        