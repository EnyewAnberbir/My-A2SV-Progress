class Solution:
    def interpret(self, command: str) -> str:
        newstr = ""
        i=0
        while i < len(command):
            if command[i] == "(" and command[i+1] == ")":
                newstr += "o"
                i+=2
            elif command[i] == "(" and command[i+1] == "a":
                newstr += "al"
                i+=4
            else:
                newstr+= command[i]
                i+=1
        return newstr
        