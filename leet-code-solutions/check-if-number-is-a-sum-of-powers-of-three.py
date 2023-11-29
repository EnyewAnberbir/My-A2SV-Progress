class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        x= int(log(n)/ log(3))

        for i in range(x, -1, -1):
            if n>= 3**i:
                n = n- 3**i
                if n==0:
                    return True
                    break
            else:
                continue
        return False
