class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtracking(start, curr):
            if len(curr) == k:
                res.append(curr[:])
                return 
            
            for num in range(start + 1, n + 1):
                curr.append(num)
                backtracking(num, curr)
                curr.pop()
        
        backtracking(0, [])

        return res
