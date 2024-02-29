# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.summ = 0

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        val = 0
        def recursive(root,i):
            nonlocal val
            if not root:
                return 
            root.val += 10*i
            recursive(root.left, root.val)
            recursive(root.right, root.val)
        def traverse(root):
            if not root:
                return
            if not root.left and not root.right:
                self.summ += root.val
                return
            traverse(root.left)
            traverse(root.right)
        recursive(root, 0)
        traverse(root)
        return self.summ

        
        
        