class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res= [[]]
        curr = []
        nums.sort()
        visited = set()
        def backtracking(index):
            
            if len(curr) > 0:
                if tuple(curr) in visited:
                    return
                visited.add(tuple(curr))
                res.append(curr[:])
            if index >= len(nums):
                return
            for i in range(index, len(nums)): 
                curr.append(nums[i])
                backtracking(i+1)
                curr.pop()
        backtracking(0)
        return res



        
        