class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #nums = [3,4,5,6]
        #target=7 

        #time complexity O(n2)
        #space complexity O(n)
        # for i in range(len(nums)):
        #     complement=target-nums[i]
        #     for j in range(i+1,len(nums)):
        #         if nums[j]==complement:
        #             return [i,j]

        #optimized approach 
        #we use a hashmap to track complements 
        # we answer the question "have I seen this complement before?"
        
        freq_nums={}
        for i in range(len(nums)):
            if target-nums[i] in freq_nums:
                return [freq_nums[target-nums[i]],i]
            else:
                freq_nums[nums[i]]=i



            



       
            
    
        

        
