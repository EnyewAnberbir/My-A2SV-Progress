# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        arr = []
        def traverse(node, ord=0):
            if node is None:
                return None

            if len(arr) == ord:
                arr.append([])
            arr[ord].append(node.val)
            traverse(node.left, ord + 1)
            traverse(node.right, ord + 1)
        
        traverse(root)
        for i in range(1, len(arr), 2):
            arr[i] = arr[i][::-1]
        return arr
