class Solution:
    def findMin(self, nums: List[int]) -> int:
        #brute force solution
        # traverse the array at any moment and find the minimum using linear search 

        # min_element=float("inf")
        # for num in nums:
        #     min_element=min(num,min_element)
        # return min_element
        

        #optimized solution:binary search 
        # we take the array, we want to rotate it any number of times  
        # example :[0,1,2,3,4,5,6] 
        # n=4 =>  [3,4,5,6,"1",2]
        # the "minimum" is the breakikng point in the array between two sorted arrays 
        # when we rotate an array the "left" portion of the array will always have more values than the tight portions


        #nums=[4,5,0,1,2,3]
        #dry run 
        #left=0 right=5 left<right=> mid=2 =>nums[mid]=0 <nums[right]=> right=1
        #left=0 right=1=> no it should be 2=> right=mid not mid-1 otherwise we exclude the mid value from the search 
        # there two key ideas for this problem:
        #rotation splits the arr

        left=0
        right=len(nums)-1               
        while left<right:
            mid = (left+right)//2
            # minimum is on the right side 
            if nums[mid]>=nums[right]:
                left=mid+1
            else:
                right=mid
        return nums[left]








