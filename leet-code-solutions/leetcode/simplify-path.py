class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        coll = {".","..", ""}
        path = path.split("/")
        for i in path:
            if i == "..":
                if stack:
                    stack.pop()
            if i not in coll :
                stack.append(i)
        print(stack)
        return "/" + "/".join(stack)
        
           
        
