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

        # This tells you where a 2D element would sit in a flattened 1D array: 
        # =>matrix_index = row * number_of_columns + col 
        # example matrix = [
            # [10, 20, 30],
            # [40, 50, 60]
            # ]
        #rows = 2
        #cols = 3
        # [10, 20, 30, 40, 50, 60]
        # index: 0   1   2   3   4   5

        #matrix[0][2] = 30 => index=0*3+2=2

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
            


        
            



        