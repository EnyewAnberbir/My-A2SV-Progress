class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        rem = {0:1}
        val = 0 
        count = 0
        for i in nums:
            val += i
            if val - k in rem:
                count += rem[val-k]
            if val in rem:
                rem[val] +=1
            else:
                rem[val] = 1

        return count