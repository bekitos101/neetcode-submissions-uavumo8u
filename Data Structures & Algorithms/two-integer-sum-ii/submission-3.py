class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #numbers = [1,2,3,4], target = 3
        #brute force approach O(n square)
        # for i in range(len(numbers)):
        #     for j in range(i+1,len(numbers)):
        #         if numbers[i]+numbers[j]==target:
        #             return [i+1,j+1]

        #optimized solution 
        #array is sorted => we can think about the two pointers


        #dRY RUN 
        #numbers=[1,2,3,4] target=3
        #left=0 right=3 nums[left]+nums[right]=5>3 => right=2 
        #left=0 right=2 nums[left]+nums[right]=4>3=>  right=1 
        #left=0 right=1 nums[left]+nums[right]=1+2=3 => return [1,2]
        left=0
        right=len(numbers)-1
        while left<right:
            if numbers[left]+numbers[right]==target:
                return [left+1,right+1]
            elif numbers[left]+numbers[right]<target:
                left+=1
            else:
                right-=1
        return []

            