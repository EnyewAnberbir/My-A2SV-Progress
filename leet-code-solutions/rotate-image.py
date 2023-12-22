class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for rows in range(len(matrix)):
            for cols in range(rows+1, len(matrix)):
                matrix[rows][cols], matrix[cols][rows] = matrix[cols][rows] , matrix[rows][cols]

            matrix[rows].reverse()
        