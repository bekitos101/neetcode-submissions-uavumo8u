class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #brute force solution 
        #height = [1,7,2,5,4,7,3,6]
        # for each height calculate all possible water amounts and keep track of the max 
        # the area is determined by the min height 

        # max_water=0
        # for i in range(len(heights)):
        #     area=0
        #     for j in range(i+1,len(heights)):
        #         area=max(area,min(heights[i],heights[j])*(j-i))
        #         max_water=max(max_water,area)
        # return max_water

        #Optimized approach 
        #key insight: the area is determined by the minimum of two heights
        #the area is limited by the shorter wall, so the only way to find the next 
        #bigger area is to keep moving the shorter wall 

        left=0
        right=len(heights)-1
        max_area=0
        while left<=right:
            area=min(heights[left],heights[right])*(right-left)
            max_area=max(max_area,area)
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1

        return max_area






