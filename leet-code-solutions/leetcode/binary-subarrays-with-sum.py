class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        rem = {0:1}
        count = 0
        val = 0
        for i in nums:
            val +=i
            if val - goal in rem:
                count += rem[val-goal]
            if val in rem:
                rem[val] += 1
            else:
                rem[val] = 1

        return count