class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Brute force solution
        #start the sequence from every number in the array 
        #keep track of the sequence length at each start 
        
        # if not nums:
        #     return 0
        # nums.sort()
        # seq=1
        # max_seq=1
        # for i in range(len(nums)-1):
        #     if nums[i+1]==nums[i]:
        #         continue
        #     elif nums[i+1]-nums[i]==1:
        #         seq+=1
        #     else:
        #         max_seq=max(max_seq,seq)
        #         seq=1
        # max_seq=max(max_seq,seq)
        # return max_seq
       
        #Optimized solution : can we solve this in O(n) ?
        # YES: the trick, we consider a numer num as the start of the sequence only if num-1 does not exist in the array 
        # lookup is usually O(n) => we can set it to O(1) by converting the array to a hashmap 
        
        if not nums:
            return 0 
        num_set=set(nums)
        max_seq=1
        for i in range(len(nums)):
            if nums[i]-1 not in num_set:
                seq=1
                curr=nums[i]
                while curr+1 in num_set:
                    seq+=1
                    curr+=1
                
                max_seq=max(max_seq,seq)
            
        return max(max_seq,seq)
                    

            
