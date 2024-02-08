class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        coll = [0]*(len(nums)+1)
        for a, b in requests:
            coll[a]+=1
            coll[b+1]-=1
        prefix_sum = [coll[0]]
        for i in range(1, len(coll)-1):
            prefix_sum.append(coll[i] + prefix_sum[i-1])
        print(prefix_sum)
        prefix_sum.sort()
        nums.sort()
        for i in range(len(nums)):
            prefix_sum[i]= prefix_sum[i]*nums[i]
        return sum(prefix_sum)%(10**9+7)