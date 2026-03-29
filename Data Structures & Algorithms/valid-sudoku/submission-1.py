class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #(0,0) => (0,0),(0,1)(0,2)
        #         (1,0),(1,1),(1,2)
        #         (2,0),(2,1),(2,2) 
        

        # starting positions in boxes 
        # (0,0) (0,3) (0,6)
        # (3,0)
        # (6,0)

        # def validate(row,col):
        #     seen=set()
        #     for i in range(row,row+3,1):
        #         for j in range(col,col+3,1):
        #             if board[i][j]==".":
        #                 continue
        #             if board[i][j] in seen:
        #                 return False
                    
        #             seen.add(board[i][j])
        #     return True 
            
        # #check rows
        # for row in board:
        #     seen_rows=set()
        #     for number in row:
        #         if number==".":
        #             continue
        #         if number in seen_rows:
        #             return False 
        #         seen_rows.add(number)
    
        # #check columns 
        # for col in range(9):
        #     #col=1
        #     seen_cols=set()
        #     for row in range(9):
        #         #row1,2,3 ..ect
        #         number=board[row][col]
        #         if number==".":
        #             continue 
        #         if number in seen_cols:
        #             return False
        #         seen_cols.add(number)
        # # check for 3x3 grids
        # for box_row in range(0,9,3):
        #     for column_row in range(0,9,3):
        #         if not validate(box_row,column_row):
        #             return False 
        # return True 


        #optimized version => only one pass 

        seen_cols=set()
        seen_rows=set()
        seen_box=set()

        for row in range(9):
            for col in range(9):
                number=board[row][col]
                
                if number== ".":
                    continue 
                
                row_check= (row,number)
                col_check=(col,number)
                # map the (r,c) into its corresponding box using integer division 
                #(4//3,7//3) => (1,2) => (1,2,5)
                box_check= (row//3,col//3,number)

                if row_check in seen_rows or col_check in seen_cols or box_check in seen_box:
                    return False 
                
                seen_rows.add(row_check)
                seen_cols.add(col_check)
                seen_box.add(box_check)
            
        return True 




        

        
        