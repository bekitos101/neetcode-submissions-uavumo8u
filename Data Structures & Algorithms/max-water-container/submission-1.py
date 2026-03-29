class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #brute force solution 
        max_area=0
        for i in range(len(heights)):
            for j in range (i+1,len(heights)):
                height=min(heights[i],heights[j])
                width=j-i
                area=height*width 
                max_area=max(max_area,area)

        return max_area


        #optimized solution 
        #height = [1,7,2,5,4,7,3,6]
        left=0
        right=len(nums)-1
        max_area=0
        while left<right:
            #calculate the area 
            height=min (heights[left],heights[right])
            width=right-left
            area=width*height
            max_area=max(max_area,area)
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
            return max_area





