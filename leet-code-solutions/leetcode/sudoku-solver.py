class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
            
    def __init__(self):
        self.size = 9
        
        self.val = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
        self.empty = '.'
        
        self.row_no = lambda cell_no: cell_no // self.size 
        self.col_no = lambda cell_no: cell_no % self.size  
        self.box_no = lambda r, c: 3 * (r // 3) + c // 3   
        
        self.row = {} 
        self.col = {}  
        self.boxVal = {}  

    def solveSudoku(self, board: List[List[str]]) -> None:
        
        for i in range(self.size):
            self.row[i] = set()
            self.col[i] = set()
            self.boxVal[i] = set()

        for r in range(self.size):
            for c in range(self.size):
                if board[r][c] != self.empty:
                    self.row[r].add(board[r][c])
                    self.col[c].add(board[r][c])
                    self.boxVal[self.box_no(r, c)].add(board[r][c])
        
        
        self.backtrack(0, board)

        return board

    def backtrack(self, cell_no, board):
        if cell_no == 81: 
            return True

        r, c = self.row_no(cell_no), self.col_no(cell_no)

        if board[r][c] != self.empty:
            return self.backtrack(cell_no + 1, board)

        for val in self.val:
            
            if val in self.row[r] or val in self.col[c] or val in self.boxVal[self.box_no(r, c)]:
                continue

       
            board[r][c] = val
            self.row[r].add(val)
            self.col[c].add(val)
            self.boxVal[self.box_no(r, c)].add(val)
            
  
            if self.backtrack(cell_no + 1, board):
                return True

       
            board[r][c] = self.empty
            self.row[r].remove(val)
            self.col[c].remove(val)
            self.boxVal[self.box_no(r, c)].remove(val)

        return False
            