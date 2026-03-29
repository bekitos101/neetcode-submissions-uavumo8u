import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:   
        frequency_dict={}
        for num in nums:
            frequency_dict[num]=frequency_dict.get(num,0)+1
        
        # we create buckets indexed by frequency: 
        buckets=[]
        for bucket in range (len(nums)+1):
            buckets.append([])
        

        for key,value in frequency_dict.items():
            idx=value
            buckets[idx].append(key)
        
        ans=[]
        for i in range(len(buckets)-1,0,-1):
            for num in buckets[i]:
                ans.append(num)
            if len(ans)==k:
                break
            
        return ans 

    
