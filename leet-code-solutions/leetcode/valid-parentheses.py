class Solution(object):
    def isValid(self, s):
        myDict = [('{', '}'), ('(', ')'), ('[', ']')]
        stack = []
        for i in s:
            if len(stack)>0 and (stack[-1], i) in myDict:
                stack.pop()
            else:
                stack.append(i)
        return len(stack)==0
        
        