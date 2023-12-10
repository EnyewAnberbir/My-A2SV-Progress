class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res =[]
        for i in nums:
            if nums.count(i) > (len(nums) //3):
                if i not in res:

                    res.append(i)
            
        return res