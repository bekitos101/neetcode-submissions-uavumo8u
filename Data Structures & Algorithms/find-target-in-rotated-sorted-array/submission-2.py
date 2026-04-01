class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # what we need to know is that at any moment , ONE SIDE IS ALWAYS SORTED 
        # the idea of this problem is that we either find the sorted side after rotation 
        #example: [4,5,6,7,0,1,2]


        left=0 
        right=len(nums)-1

        while left<=right:
            mid=(left+right)//2 
            if nums[mid]==target:
                return mid 
            #left side is sorted 
            elif nums[left]<=nums[mid]:
                #is my target in this side? 
                if nums[left]<=target<nums[mid]:
                    #we go more left
                    right=mid-1
                else:
                    left=mid+1
            else:
                if nums[mid]<target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1
        return -1 
            

               