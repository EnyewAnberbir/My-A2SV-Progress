class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        coll = [nums[0]]
        for i in range(1, len(nums)):
            coll.append(coll[-1] + nums[i]) 
        return coll