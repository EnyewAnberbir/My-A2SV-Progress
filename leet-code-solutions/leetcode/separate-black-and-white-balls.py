class Solution:
    def minimumSteps(self, s: str) -> int:
        i = 0
        j = len(s)-1
        summ = 0
        while i < j:
            if s[i] == "1" and s[j] == "0":
                summ += j-i
                i+=1
                j-=1
            elif s[i] == "0" and s[j] != "1":
                i+=1
            elif s[j] == "1" and s[i] != "0":
                j-=1
            else:
                i+=1
                j-=1
        return summ

        