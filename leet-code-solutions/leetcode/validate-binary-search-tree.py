# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxi = 0
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []
        def recursive(root):
            if not root:
                return True
            recursive(root.left)
            arr.append(root.val)
            recursive(root.right)
        recursive(root)
        if arr == sorted(arr):
            for i in range(len(arr)-1):
                if arr[i] == arr[i+1]:
                    return False
            return True
        else:
            return False