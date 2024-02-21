class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def recursive(left, right):
            if left > right:
                return 0
            
            
            return max(nums[left] - recursive(left+1, right),nums[right] - recursive(left, right-1))
            
        return recursive(0, len(nums)-1) >= 0