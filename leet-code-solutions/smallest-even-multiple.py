class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n %2 !=0:
            return n*2
        else:
            for i in range(1, n+1):
                if (i*2) % n == 0:
                    return i*2
                    break



                
        
                    
