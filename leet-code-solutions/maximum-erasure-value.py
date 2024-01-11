class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ref = {}
        left = 0
        maxsum = 0
        for right in range(len(nums)):
            if nums[right] in ref and ref[nums[right]] >= left:
                left = ref[nums[right]]+1
            
            ref[nums[right]] = right
            maxsum = max(maxsum , sum(nums[left:right+1]))

        return maxsum

