class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [] 
        res = 0 
        for idx, char in enumerate(s): 
            if char == '(': 
                stack.append(0)
            elif char == ')': 
                temp = stack.pop()
                if temp == 0: 
                    temp += 1 
                else: 
                    temp *= 2 
                if stack: 
                    stack[-1] += temp
                else: 
                    res += temp
        
        return res