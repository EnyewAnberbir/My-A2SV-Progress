class Solution:
    def isHappy(self, n: int) -> bool:
        myDict = set()
    
        while n != 1 and n not in myDict:
            myDict.add(n)
            n = sum(int(i) ** 2 for i in str(n))
        
        return n == 1
        
        





        

            


        
        