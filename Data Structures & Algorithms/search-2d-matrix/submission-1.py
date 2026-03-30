class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #brute force solution 
        # n=len(matrix)
        # m=len(matrix[0])
        # for i in range(n):
        #     for j in range(m):
        #         if matrix[i][j]==target:
        #             return True 
        # return False 
        
        #optimized solution 
        
        rows=len(matrix)
        cols=len(matrix[0])

        left=0
        right=rows*cols-1

        # when a 2D matrix is sorted =>matrix_index = row * n + col 
        # n= number of columns 
        while left<=right: 
            mid=(left+right)//2 
            row=mid // cols
            column=mid % cols
            val=matrix[row][column]

            if val==target:
                return True
            elif val<target:
                left=mid+1
            else:
                right=mid-1
        
        return False  
            


        
            



        