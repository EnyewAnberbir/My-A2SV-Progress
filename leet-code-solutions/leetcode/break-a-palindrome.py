class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        coll = []
        for i in palindrome:
            coll.append(i)
        if len(coll) == 1:
            return ""
        i = 0
        while i < len(coll)//2:
            if coll[i] == "a":
                i+=1
            else:
                coll[i] = "a"
                return "".join(coll)
        coll[len(coll)-1] = "b"
        return "".join(coll)
        
       
            

        