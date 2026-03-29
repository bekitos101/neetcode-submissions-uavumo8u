import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:   
        frequency_dict={}
        for num in nums:
            frequency_dict[num]=frequency_dict.get(num,0)+1
        heap=[]
        for key,value in frequency_dict.items(): 
            if len(heap)<k:
                heapq.heappush(heap,(value,key))
            else:
                heapq.heappushpop(heap,(value,key))
        ans=[]
        for h in heap:
            ans.append(h[1])
        return ans