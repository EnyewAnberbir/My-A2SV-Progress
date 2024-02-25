class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            oper = '-+/*'
            if t not in oper:
                stack.append(int(t))
            else:
                a, b = stack.pop(), stack.pop()
                if t == "+":
                    stack.append(b+a)
                elif t == "-":
                    stack.append(b-a)
                elif t == "*":
                    stack.append(b*a)
                else:
                    stack.append(int(float(b)/a))
        return stack.pop()

   
                
        
        