class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        target = n * (n + 1) // 2  

        actual = sum(nums)

        return target - actual
                

        