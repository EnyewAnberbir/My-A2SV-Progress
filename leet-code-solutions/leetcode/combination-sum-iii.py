class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        curr = []
        def backtracking(index):
            if len(curr) == k and sum(curr)==n:
                res.append(curr[:])
                return
            if len(curr) > k or index > n:
                return 
            for i in range(index, 10):
                curr.append(i)
                backtracking(i+1)
                curr.pop()
        backtracking(1)
        return res
        