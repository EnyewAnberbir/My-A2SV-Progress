class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        myDict = {num: i for i, num in enumerate(nums)}

        for i, j in operations:
            index = myDict[i]
            nums[index] = j
            del myDict[i]
            myDict[j] = index

        return nums
            