class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        if n%2 == 0:
            even = n//2
            odd = n//2
        else:
            even = n//2 + 1
            odd = n//2
        def recursive(num,exponent):
            if exponent <= 0:
                return 1
            elif exponent % 2 == 0:
                A = recursive(num, (exponent//2))
                return A**2 % MOD
            else:
                B = recursive(num, (exponent//2))
                return (num * (B **2)% MOD )% MOD
        return (recursive(5, even) * recursive(4,odd))%MOD




                        