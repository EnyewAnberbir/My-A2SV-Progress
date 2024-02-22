class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix_sum = [0] * (len(nums) + 1)

        
        for i in range(len(nums)):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        maxx = float('-inf')
        mini = 0

        for i in range(1, len(prefix_sum)):
            maxx = max(maxx, prefix_sum[i] - mini)
            mini = min(mini, prefix_sum[i])

        return maxx
        