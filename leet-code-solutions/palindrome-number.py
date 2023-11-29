class Solution:
    def isPalindrome(self, x: int) -> bool:

        temp = str(x)
        rev = temp[::-1]

        if temp == rev:
            return True
        else:
            return False
    
