class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_box(start_row,start_column):
            seen=set()
            for i in range(start_row,start_row+3,1):
                for j in range(start_column,start_column+3,1):
                    if board[i][j]==".":
                        continue
                    if board[i][j] in seen:
                        return False 
                    seen.add(board[i][j])
            return True 

        #validate rows
        for row in board:
            seen_rows=set()
            for item in row:
                if item==".":
                    continue 
                if item in seen_rows:
                    return False 
                seen_rows.add(item)

        #validate columns
        # 0,0       0,1
        # 1,0       1,1
        # 2,0       2,1
        # 3,0       3,1  
        # ...      .... 
        for i in range(9):
            seen_cols=set()
            for j in range(9):
                item=board[j][i]
                if item==".":
                    continue
                if item in seen_cols:
                    return False 
                seen_cols.add(item)
        
        #validate boxes
        #boxes bounds 
        # 0,0 0,1  0,2     #0,3    0,5     #0,6     0,8
        # 1,0 1,1  1,2
        # 2,0 2,1  2,2     #2,3    2,5     #2,6     2,8 
        
        for i in range(0,9,3):
            for j in range(0,9,3):
                if not check_box(i,j):
                    return False 
    
        return True 

        


                

            


        

        



        

        
        