class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #brute force solution 
        #traverse the array and for each number in the array calculate the product of everything except that number
        # TC O(n2) SC (On)
        # output=len(nums)*[0]
        # for i in range(len(nums)):
        #     product=1
        #     for j in range(len(nums)):
        #         if i!=j:
        #             product*=nums[j]
        #     output[i]=product
        # return output

        output=len(nums)*[0]

        #optimized approach 
        #we can construct two arrays , one calculate the product on the right of any number(suffix)
        # one calculate the product on the left of any number
        #output = the product of these two arrays 

        #construct suffix
        # nums = [1,2,4,6]
        # suffix=[48,24,6,1]
        #1 (suffix[3])=1 (initialized)
        #6(suffix[2])=6*1=nums[3]xsuffix[3]
        #24(suffix[1])=nums[2]*suffix[2]
        #48(suffix[0])=nums[1]*suffix[1]

        suffix=[1]*len(nums)
        for i in range(len(nums)-2,-1,-1):
            suffix[i]=nums[i+1]*suffix[i+1]

        #construct prefix 
        #nums = [1,2,4,6]
        #prefix=[1,1,2,8]

        #1=1 (inialiazed)
        #prefix[1]=prefix[0]*nums[0]
        #prefix[2]=prefix[1]*nums[1] ..ect
        prefix=[1]*len(nums)
        for i in range(1,len(nums),1):
            prefix[i]=prefix[i-1]*nums[i-1]
        
        for i in range(len(nums)):
            output[i]=prefix[i]*suffix[i]
        return output

        #TC O(n) SC O(n)


            




        