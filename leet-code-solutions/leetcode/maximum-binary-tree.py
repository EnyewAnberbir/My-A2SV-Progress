# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        half = max(nums)
        middle = nums.index(half)

        left = self.constructMaximumBinaryTree(nums[:middle])
        right = self.constructMaximumBinaryTree(nums[middle+1:])

        return TreeNode(nums[middle], left, right)