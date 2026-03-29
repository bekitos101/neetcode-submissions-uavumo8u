class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequency_dict={}
        for num in nums:
            frequency_dict[num]=frequency_dict.get(num,0)+1

        sorted_freq=sorted(frequency_dict.items(),key= lambda item:item[1],reverse=True )

        res=[]
        for i in range(k):
            res.append(sorted_freq[i][0])
        return res
