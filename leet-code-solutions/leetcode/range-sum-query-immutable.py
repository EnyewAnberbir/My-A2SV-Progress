class NumArray:

    def __init__(self, nums: List[int]):
        self.summ = [0]
        for i in nums:
            self.summ.append(self.summ[-1]+ i)
        
    def sumRange(self, left: int, right: int) -> int:
        return self.summ[right+1] - self.summ[left]
        


