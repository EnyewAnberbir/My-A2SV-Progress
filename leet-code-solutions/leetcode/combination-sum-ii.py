class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        candidates.sort()
        def backtracking(index):
            temp = sum(curr)
            if temp == target:
                res.append(curr[:])
                return
            if temp > target or index > len(candidates):
                return
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                curr.append(candidates[i])
                backtracking(i+1)
                curr.pop()
        backtracking(0)
        return res
