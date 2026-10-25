class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        nums= [1,2,3,4,5,6,7,8]   k=4
        iter1=[8,1,2,3,4,5,6,7]   k=3
        iter2=[7,8,1,2,3,4,5,6]   k=2 
        iter3=[6,7,8,1,2,3,4,5]   k=1 
        iter4=[5,6,7,8,1,2,3,4]   k=0
        

        nums=[1,2,3,4,5,6,7,8]
        reverse=[8,7,6,5,4,3,2,1]
        reverse2=[[5,6,7,8],[1,2,3,4]]

        '''

        # n=len(nums)
        # for i in range(k):
        #     last=nums[n-1]
        #     for j in range(n-1,0,-1):
        #         nums[j]=nums[j-1]
        #     nums[0]=last
        
        
        n=len(nums)
        k=k%n
        def reverse(left,right):
            while left<right:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right-=1
        
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)









