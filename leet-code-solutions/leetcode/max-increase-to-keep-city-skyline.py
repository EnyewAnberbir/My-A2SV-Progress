class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        # Calculate maximum values for each row
        maxrow = []
        for row in grid:
            maxrow.append(max(row))
        maxcol = []
        for j in range(len(grid[0])):
            maxcol.append(max(grid[i][j] for i in range(len(grid))))
        temp = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                temp += min(maxrow[i], maxcol[j]) - grid[i][j]
        
        return temp
