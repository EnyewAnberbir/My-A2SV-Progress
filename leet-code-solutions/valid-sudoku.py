class Solution:
  def isValidSudoku(self, board: List[List[str]]) -> bool:
    checked = set()

    for i in range(9):
      for j in range(9):
        c = board[i][j]
        if c == '.':
          continue
        if c + '@row ' + str(i) in checked or \
           c + '@col ' + str(j) in checked or \
           c + '@box ' + str(i // 3) + str(j // 3) in checked:
          return False
        checked.add(c + '@row ' + str(i))
        checked.add(c + '@col ' + str(j))
        checked.add(c + '@box ' + str(i // 3) + str(j // 3))

    return True