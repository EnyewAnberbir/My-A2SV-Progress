class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        temp = 0
        minlen = float("inf")
        for right in range(len(nums)):
            temp += nums[right]
            while temp >= target:
                minlen = min(minlen, right-left+1)
                temp-= nums[left]
                left+=1
            
        if minlen == float("inf"):
            return 0
        else:
            return minlen
            
        
            

        