class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        sol = []
        i = 0
        j = 1
        while i < len(nums)-1 and j < len(nums):
            for k in range(nums[i]):
                sol.append(nums[j])
            i+=2
            j+=2
        return sol
            
        