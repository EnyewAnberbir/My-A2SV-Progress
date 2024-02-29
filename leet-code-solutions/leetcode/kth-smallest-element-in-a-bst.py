# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: 
    def __init__(self):
        self.mini = float("inf")
        # self.arr = []
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def recursive(root,k):
            if root is None:
                return None
            
            recursive(root.left,k)
            arr.append(root.val)
            recursive(root.right,k)
        recursive(root,k)
        print(arr)
        return arr[k-1]
        

            


        