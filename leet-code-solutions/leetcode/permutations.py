class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) == 1:
            return [nums[:]]
        for i in range(len(nums)):
            a = nums.pop(0)
            temp = self.permute(nums)
            for i in temp:
                i.append(a)
            res.extend(temp)
            nums.append(a)
        return res
            
            
        