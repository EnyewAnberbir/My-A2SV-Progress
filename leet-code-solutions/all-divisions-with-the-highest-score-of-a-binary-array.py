class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        zero = nums.count(0)
        one = len(nums)- zero
        count1 = 0
        count2 = 0
        res = [0]
        maxval= one
        for i , num in enumerate(nums):
            count1 += num == 0
            count2 += num == 1
            right = one - count2
            val = count1 + right
            if maxval == val:
                res.append(i+1)
            elif maxval < val:
                maxval = val
                res = [i+1]
        return res
            
            
            
                





            
        
        
            
            
