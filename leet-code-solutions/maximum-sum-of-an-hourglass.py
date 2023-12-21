class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        maxsum = float("-inf")
        def their_sum(i , j):
            return (
                grid[i][j] + grid[i][j+1] + grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]
            )
        for a in range(len(grid)-2): 
            for b in range(len(grid[0])-2):
                temp = their_sum(a , b)
                maxsum = max(maxsum, temp)

        return maxsum

                



        
        