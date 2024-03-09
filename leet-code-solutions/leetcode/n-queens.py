class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [["."]*n for i in range(n)]

        def backtracking(row,cols,label1,label2):
            if row == n:
                result.append(["".join(line) for line in board])
                return
            for col in range(n):
                if col not in cols and row+col not in label1 and row-col not in label2:
                    board[row][col] = "Q"
                    backtracking(row+1, cols|set([col]), label1|set([row+col]), label2|set([row-col]))
                    board[row][col] = "."
        backtracking(0,set(),set(),set())
        return result