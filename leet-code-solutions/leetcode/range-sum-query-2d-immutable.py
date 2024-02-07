class NumMatrix:
  def __init__(self, matrix: List[List[int]]):
    len1 = len(matrix)
    len2 = len(matrix[0])
    self.prefix = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    for i in range(len1):
      for j in range(len2):
        self.prefix[i + 1][j + 1] = matrix[i][j] + self.prefix[i][j + 1] + self.prefix[i + 1][j] - self.prefix[i][j]

  def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
    return self.prefix[row2 + 1][col2 + 1] - self.prefix[row1][col2 + 1] -self.prefix[row2 + 1][col1] + self.prefix[row1][col1]