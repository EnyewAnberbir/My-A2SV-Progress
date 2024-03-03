class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = []
        def backtracking(count_o, count_c):
            if len(curr) == 2*n:
                res.append("".join(curr))
                return
            if count_o:
                curr.append("(")
                backtracking(count_o-1, count_c)
                curr.pop()

            if count_c  > count_o:
                
                curr.append(")")
                backtracking(count_o, count_c-1)
                curr.pop()

        backtracking(n,n)
        return res


       