class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans,positive,negative = [],[],[]
    

        for num in nums:
            (positive if num > 0 else negative).append(num)

        for p, n in zip(positive, negative):
            ans += [p, n]

        return ans