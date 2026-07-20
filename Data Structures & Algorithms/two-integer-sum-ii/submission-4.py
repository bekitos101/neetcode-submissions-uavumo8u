class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #Brute force solution 
        #numbers = [1,2,3,4]  target = 3
        for i in range(len(numbers)):
            complement=target-numbers[i]
            for j in range(i,len(numbers)):
                if numbers[j]==complement:
                    return [i+1,j+1]

            