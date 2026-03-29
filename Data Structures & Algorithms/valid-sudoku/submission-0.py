class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #(0,0) => (0,0),(0,1)(0,2)
        #         (1,0),(1,1),(1,2)
        #         (2,0),(2,1),(2,2) 
        

        def validate(row,col):
            seen=set()
            for i in range(row,row+3,1):
                for j in range(col,col+3,1):
                    number
                    if board[i][j]==".":
                        continue
                    if board[i][j] in seen:
                        return False
                    
                    seen.add(board[i][j])
            return True 
            
        #check rows
        for row in board:
            seen_rows=set()
            for number in row:
                if number==".":
                    continue
                if number in seen_rows:
                    return False 
                seen_rows.add(number)
    
        #check columns 
        for col in range(9):
            seen_cols=set()
            for row in range(9):
                number=board[row][col]
                if number==".":
                    continue 
                if number in seen_cols:
                    return False
                seen_cols.add(number)
        # check for 3x3 grids
        for box_row in range(0,9,3):
            for column_row in range(0,9,3):
                if not validate(box_row,column_row):
                    return False 
        return True 
                
        
        