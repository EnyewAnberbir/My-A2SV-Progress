# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # def access(root):
        #     if root is None:
        #         return root
        #     access(root.left)
        #     access(root.right)
          
        if root is None:
            return None
        
        if val == root.val:
            print(root)
            self.ans.append(root)
        elif val < root.val:
            self.searchBST(root.left,val)
        else:
            self.searchBST(root.right,val)
        return self.ans[0] if self.ans else None
    


        

                


        