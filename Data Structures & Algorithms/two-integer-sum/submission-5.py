class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums=[3,4,5,6] target=7 
        # Brute force solution : check every pair in the array
        # for i in range (len(nums)):
        #     complement=target-nums[i]
        #     for j in range(i+1,len(nums)):
        #         if nums[j]==complement:
        #             return [i,j]
        # return [] 

        #optimized approach : can we use another data structure ?
        # hashmap answers the "have I seen x ?" in O(1) time  
        # for each element, we try to remember if we have seen its complement before in the hashmap 
        # otherwise, we store it in the hashmap 
        # we are using a hashmap instead of a set because we need the pair "complement:"index"

        complement_map={}
        for i in range(len(nums)):
            complement=target-nums[i]
            if complement in complement_map:
                return [complement_map[complement],i]
            complement_map[nums[i]]=i

            
    
        

        
