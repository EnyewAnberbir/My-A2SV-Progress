# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = 0
        def recursive(node, maxi=float("-inf"), mini=float("inf")):
            nonlocal res
            if not node: 
                return None
            maxi = max(maxi, node.val)
            mini = min(mini, node.val)

            res = max(res, maxi - mini)

            recursive(node.left, maxi, mini)
            recursive(node.right, maxi, mini)
        
        
        recursive(root)
        return res