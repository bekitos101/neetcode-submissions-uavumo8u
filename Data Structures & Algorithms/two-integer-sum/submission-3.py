class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #brute force solution 
        # nums = [3,4,5,6], target = 7
        # check each pair of the array 
        # for i,num in enumerate(nums):
        #     rest=target-num 
        #     for j in range(i+1,len(nums)):
        #         if nums[j]==rest:
        #             return [i,j]
                    

        
   

        #hash_map={4:0,3:1,2:3,1:4}
        

        #i=0 num=3
        #target-num=4 
        diff_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in diff_map:
                return [diff_map[complement], i]
            diff_map[num] = i

        # diff_map={}
        # for i,num in enumerate(nums):
        #     diff_map[num]=i 
        
        # for i,num in enumerate(nums):
        #     complement= target -num 
        #     if complement in diff_map and diff_map[complement] != i:
        #         return [i,diff_map[complement]]

        
