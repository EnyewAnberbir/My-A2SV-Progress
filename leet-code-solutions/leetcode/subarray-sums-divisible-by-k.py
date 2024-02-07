class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ref  = {0:1}
        count = 0
        summ = 0
        for i in nums:
            summ += i
            temp = summ % k
            if temp < 0:
               temp += k
            if summ % k in ref:
                count += ref[temp]
            if summ % k in ref:
                ref[summ%k] += 1
            else:
                ref[summ%k] = 1
        return count
                
        