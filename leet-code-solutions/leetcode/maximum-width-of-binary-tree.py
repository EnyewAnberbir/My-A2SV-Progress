# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        val=[(root,0)]
        width=1
        while len(val)!=0:
            if len(val)>1:
                width=max(width,val[-1][1]-val[0][1]+1)

            temp_val=[]
            while len(val)!=0:
                node,position=val.pop(0)

                if node.left!=None:
                    temp_val.append((node.left,position*2))

                if node.right!=None:
                    temp_val.append((node.right,position*2+1))

            val=temp_val                    
        
        return width