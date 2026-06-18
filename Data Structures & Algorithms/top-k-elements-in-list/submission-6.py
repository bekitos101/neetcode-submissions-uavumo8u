import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Brute force solution:
        #traverse the array, for each distinct element we get the count
        #store these in a frequency map 
        # return the elements with the K top frequent elements from the frequency map 

        freq_count={}

        for num in nums:
            freq_count[num]=freq_count.get(num,0)+1
        
        #[1:1,2:2,3:3] k=2

        freq_sorted = sorted(freq_count.items(), key=lambda item: item[1],reverse=True)

        print(freq_sorted)
        result=[]

        count=0

        for item in freq_sorted:
            result.append(item[0])
            count+=1
            if count==k:
                break
        return result 
        
        #time complexity



       