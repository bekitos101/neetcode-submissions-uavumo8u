class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Brute force solution
        #start the sequence from every number in the array 
        #keep track of the sequence length at each start 
        
        if not nums:
            return 0
        nums.sort()

        seq=1
        max_seq=1
        for i in range(len(nums)-1):
            if nums[i+1]==nums[i]:
                continue
            elif nums[i+1]-nums[i]==1:
                seq+=1
            else:
                max_seq=max(max_seq,seq)
                seq=1
        max_seq=max(max_seq,seq)

        return max_seq
       
            
