# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        points = []
        def recursive(root, row, col):
            if root is None:
                return
            
            left = recursive(root.left, row+1, col-1)
            right = recursive(root.right, row+1, col+1)

            points.append([col, row, root.val  ])
        recursive(root,0,0)
        points.sort()
        result = []
        i = 0
        while i < len(points):
            coll = []
            col = points[i][0]
            while i < len(points) and points[i][0] == col:
                coll.append(points[i][2])
                i += 1
            result.append(coll)
        return result