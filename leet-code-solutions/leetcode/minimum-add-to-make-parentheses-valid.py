class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        count1 = 0
        for i in range(len(s)):
            if s[i] == "(":
                count +=1
            elif s[i] == ")" and count == 0:
                count1+=1
            else:
                count-=1
        return abs(count+count1)


            

        