class Solution:
    def myPow(self, x: float, n: int) -> float:
        def recursive(num,exponent):
            if exponent <= 0:
                return 1
            elif exponent % 2 == 0:
                A = recursive(num, (exponent//2))
                return A**2 
            else:
                B = recursive(num, (exponent//2))
                return (num * (B **2))
        if n < 0:
            return (recursive(1/x, abs(n)) )
        return (recursive(x, n))
        