class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        tot = sum(nums)
        left = 0

        for i in range(n):
            if left == tot - left - nums[i]:
                return i
            left += nums[i]

        return -1