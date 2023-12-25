class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        myDict = []
        summ = 0
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if row - col == 0:
                    if (row,col) not in myDict:
                        myDict.append((row,col))
                        summ += mat[row][col]
                elif row + col == len(mat)-1:
                    if (row,col) not in myDict:
                        myDict.append((row,col))
                        summ += mat[row][col]
        return summ

                    

                

            

                
        