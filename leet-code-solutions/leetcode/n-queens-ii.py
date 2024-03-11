class Solution:
    def totalNQueens(self, n: int) -> int:
        def helper(board, row, col):
            for x in range(row):
                if board[x][col] == 'Q':
                    return False
                if col - (row - x) >= 0 and board[x][col - (row - x)] == 'Q':
                    return False
                if col + (row - x) < n and board[x][col + (row - x)] == 'Q':
                    return False
            return True
        self.ans = 0
        
        def backtrack(row):
            if row == n:
                self.ans += 1
                return
            for col in range(n):
                if helper(board, row, col):
                    board[row][col] = 'Q'
                    backtrack(row + 1)
                    board[row][col] = '.'
        board = [['.' for _ in range(n)] for _ in range(n)]
        solutions = []
        backtrack(0)
        return self.ans