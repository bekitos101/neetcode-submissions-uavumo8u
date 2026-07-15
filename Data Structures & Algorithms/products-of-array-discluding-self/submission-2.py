class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #brute force solution 
        #traverse the array and for each number in the array calculate the product of everything except that number
        output=len(nums)*[0]
        for i in range(len(nums)):
            product=1
            for j in range(len(nums)):
                if i!=j:
                    product*=nums[j]
            output[i]=product
        return output

        #dry run 
        #i=0 product =0 
        #    j=0 skip 
        #    j=1 product
                    


        