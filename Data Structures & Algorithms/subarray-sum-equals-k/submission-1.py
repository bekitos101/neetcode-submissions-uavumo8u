class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # nums = [1,1,1] k=2 

        # count = 0     
        # for i in range(len(nums)):
        #     current_sum = 0   # reset for each start
        #     for j in range(i, len(nums)):
        #         current_sum += nums[j]   # grow subarray 
        #         if current_sum == k:
        #             count += 1
        # return count
        
        #here we are recomputing subarrays again 
        #we want to reuse the previous work 
        #this is where the prefix sum and hashmap comes in 
        
        #instead of restarting each time => keep one running sum => prefix_sum+=num

        count=0
        prefix_sum=0 
        seen={0:1} # frequency of previous sums 

        #we have sum from 0 to i => prefix sum[i]

        #for j>i we have sum from 0 to j => prefix sum[j]

        #sum from i+1 to j gives us prefix_sum[j]-prefix_sum[i]

        # we want the sum from i+1 to j to be =k 

        # so we look for i such as prefix_sum[j]-k already exists => prefix_sum[i] is already computed 

        for num in nums:
            prefix_sum+=num 

            #if we see the prefix_sum[j]-k in the hashmap => it means subarray sum from i+1 to j is k 
            if prefix_sum-k in seen:
                count+=seen[prefix_sum-k]


            #each time we add the computed sum to the hashmap     
            seen[prefix_sum]=seen.get(prefix_sum,0)+1

        return count


