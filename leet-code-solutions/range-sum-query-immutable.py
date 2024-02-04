class NumArray:

    def __init__(self, nums: List[int]):
        self.summ = [0]
        for num in nums:
            self.summ.append(self.summ[-1]+num)
        
    def sumRange(self, left: int, right: int) -> int:
        return self.summ[right+1] - self.summ[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)