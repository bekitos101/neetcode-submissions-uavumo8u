class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[l] <= nums[m] > nums[r]:
                # that means the pivot is to the right of m
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[l] > nums[m] <= nums[r]:
                # that means the pivot is to the left of m
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                # that means it is sorted correctly and we can perform normal binary search
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
        
        # if target is still not found return -1
        return -1