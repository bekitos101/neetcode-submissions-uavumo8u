class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #nums = [3,4,5,6]
        #target=7 

        for i in range(len(nums)):
            complement=target-nums[i]
            for j in range(i+1,len(nums)):
                if nums[j]==complement:
                    return [i,j]

        
       
            
    
        

        
