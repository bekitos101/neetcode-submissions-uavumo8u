class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums=[3,4,5,6] target=7 
        # Brute force solution : check every pair in the array
        # Debug: 
        # nums=[3,4,5,6] target=7  
        # i=0, complement=7-nums[0]=7-3 =4, j=1
        for i in range (len(nums)):
            complement=target-nums[i]
            for j in range(i+1,len(nums)):
                if nums[j]==complement:
                    return [i,j]
        return []


        

        
