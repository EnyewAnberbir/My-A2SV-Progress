class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        summ = 0
        count = 0
        i = 0
        while summ < n:
            if i < len(nums) and nums[i] <= summ + 1:
                summ += nums[i]
                i += 1
            else:
                summ += (summ + 1)
                count += 1

        return count