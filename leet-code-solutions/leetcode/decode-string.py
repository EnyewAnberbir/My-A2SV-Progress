class Solution:
    def decodeString(self, s: str) -> str:

        def recursion(s):

            if '[' not in s:
                return s
            
            left = s.index('[')
            right = -1
            
            n_open = 1
            for i in range(left+1, len(s)):
                if s[i] == '[':
                    n_open += 1
                elif s[i] == ']':
                    n_open -= 1
                
                if n_open == 0:
                    right = i
                    break
            
            n_index = 0
            for j in range(left):
                if s[j].isdigit():
                    n_index = j
                    break
            
            s1 = s[:n_index]
            n = int(s[n_index:left])
            s2 = s[left+1: right]
            s3 = s[right+1:]
        
            return recursion(s1) + n*recursion(s2) + recursion(s3)
        return recursion(s)