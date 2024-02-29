class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        prefix_sum = [0] * (n+1)
      
        for i in range(1,n+1):
            prefix_sum[i] = prefix_sum[i-1] + nums[i-1]
        
        for  i in range(n):
            summ = nums[i]*i - (prefix_sum[i])
            summ += (prefix_sum[n]- prefix_sum[i+1]) - (nums[i]* (n-i-1))
            res.append(summ)

        return res 
        

        