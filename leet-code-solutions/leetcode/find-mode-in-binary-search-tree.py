# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def findMode(self, root: Optional[TreeNode]) -> List[int]:
    self.ans = []
    self.temp = None
    self.count = 0
    self.maxCount = 0

    def recursive(root: Optional[TreeNode]) -> None:
      if self.temp and self.temp.val == root.val:
        self.count += 1
      else:
        self.count = 1

      if self.count > self.maxCount:
        self.maxCount = self.count
        self.ans = [root.val]
      elif self.count == self.maxCount:
        self.ans.append(root.val)

      self.temp = root

    def recursive1(root: Optional[TreeNode]) -> None:
      if not root:
        return

      recursive1(root.left)
      recursive(root)
      recursive1(root.right)

    recursive1(root)
    return self.ans
        