class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums = [2,20,4,10,3,4,5]
        #sort ? 
        # [2,3,4,4,5,10,20]
        #[2,3,4,5,10,20]
        #longest squence: [2,3,4,5]=> res=4 

        #nums = [0,3,2,5,4,6,1,1]
        #nums=[0,1,1,2,3,4,5,6]
        
        #Dry Run 
        #nums=[0,3,2,5,4,6,1,1]
        #sort:[0,1,1,2,3,4,5,6]
        #i=0 => nums[0]=0 nums[1]=1 => sequence=2 
        #i=1 => nums[1]=1 nums[2]=1 => skip 
        #i=2=> nums[2]=1 nums[3]=2 => sequence=3 
        #i=3 => nums[3]=2 nums[4]=3 => sequence =4 
        #i=4 => nums[4]=3 nums[5]=4 => sequence=5 
        #i=5 => nums[5]=4 nums[6]=5=> sequence=6
        #i=6 => nums[6]=5 nums[7]=6 => sequence=7 

        if not nums:
            return 0 
            
        # nums.sort(reverse=False)
        # max_consecutive_sequence=0
        # sequence=1
        # for i in range(0,len(nums)-1):
        #     if nums[i]==nums[i+1]:
        #         continue     
        #     if nums[i+1]==nums[i]+1:
        #         sequence+=1
        #     else:
        #         max_consecutive_sequence=max(sequence,max_consecutive_sequence)
        #         sequence=1
        # return max(max_consecutive_sequence,sequence) 

        
        nums_set=set(nums)
        max_sequence=0
        for num in nums_set: 
            if num-1 not in nums_set:
                current_seq=1
                current=num
                while current+1 in nums_set:
                    current_seq+=1
                    current+=1
                max_sequence=max(max_sequence,current_seq)
        
        return max(max_sequence,current_seq)

            
            
