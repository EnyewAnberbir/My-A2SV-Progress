class Solution(object):
    def isPowerOfThree(self, n):
        if n == 0:
            return False
        if n == 1:
            return True
        if n % 3 != 0:
            return False
        return True and self.isPowerOfThree(n/3)