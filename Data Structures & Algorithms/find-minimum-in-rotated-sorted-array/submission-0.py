class Solution:
    def findMin(self, nums: List[int]) -> int:
        #brute force solution
        # traverse the array at any moment and find the minimum using linear search 

        min_element=float("inf")
        for num in nums:
            min_element=min(num,min_element)
        return min_element
        