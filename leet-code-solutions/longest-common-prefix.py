class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        x = strs[0]
        y = strs[-1]
        com = ""
        for i in range(len(x)):
            if i < len(y) and x[i] == y[i]:
                com += x[i]
            else:
                break

        return com

            

                
                
                

                
        


        
    
        