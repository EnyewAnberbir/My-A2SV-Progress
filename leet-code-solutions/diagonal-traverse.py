class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m,n = len(mat), len(mat[0])
        res = []
        for i in range(m+n-1):
            if i % 2 ==0:
                row, col = min(i, m-1), max(0, i-m +1)
                while row >= 0 and col < n:
                    res.append(mat[row][col])
                    row -= 1
                    col += 1
            else:
                row, col = max(0, i-n+1), min(i, n-1)
                while row<m and col >= 0:
                    res.append(mat[row][col])
                    row += 1
                    col -= 1
                
        return res

        
        