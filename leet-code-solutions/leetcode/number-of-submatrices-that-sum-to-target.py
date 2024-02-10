class Solution:
  def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
    m = len(matrix)
    n = len(matrix[0])
    ans = 0
    for r in matrix:
      for i in range(1, n):
        r[i] += r[i - 1]

    for temp in range(n):
      for j in range(temp, n):
        count = collections.Counter({0: 1})
        summ = 0
        for i in range(m):
          if temp > 0:
            summ -= matrix[i][temp - 1]
          summ += matrix[i][j]
          ans += count[summ - target]
          count[summ] += 1

    return ans