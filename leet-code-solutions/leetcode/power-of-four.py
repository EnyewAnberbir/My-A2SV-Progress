class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def recursive(num):
            if num == 1:
                return True
            elif num < 1:
                return False
            return recursive(num/4)
        
        return recursive(n)
                
        