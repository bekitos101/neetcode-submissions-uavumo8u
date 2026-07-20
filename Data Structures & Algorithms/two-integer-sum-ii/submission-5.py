class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #Brute force solution 
        #numbers = [1,2,3,4]  target = 3
        #we do not use the fact that the array is sorted 
        #dummy solution is just to traverse the array and return the indices(+1) since it's 1-indexed 
        
        # for i in range(len(numbers)):
        #     complement=target-numbers[i]
        #     for j in range(i,len(numbers)):
        #         if numbers[j]==complement:
        #             return [i+1,j+1]

        #Optimal solution: can we use the fact that the array is sorted ? 
        #This is a search problem , so we would like nums[index1]+nums[index2]==target
        #since the array is sorted, we can assign a two pointer approach
        # nums[index1]+nums[index2]>target => we move right
        # nums[index1]+nums[index2]<target=> we move left 

        left=0 
        right=len(numbers)-1
        while left<=right:
            if numbers[left]+numbers[right]==target:
                return [left+1,right+1]
            elif numbers[left]+numbers[right]>target:
                right-=1
            else:
                left+=1
        

            