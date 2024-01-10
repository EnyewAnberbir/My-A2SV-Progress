class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        temp = sum(nums[:k-1])
        maxval =float("-inf")
        for right in range(k-1, len(nums)):
            temp += nums[right]
            maxval = max(temp, maxval)
            temp -= nums[right-k+1]
        return maxval/k




        